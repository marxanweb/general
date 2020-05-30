#utiliy for updating all of the marxan servers databases from a single script
import requests, json, os
from requests.exceptions import ConnectTimeout, SSLError, RequestException, ConnectionError
MARXAN_REGISTRY = "https://marxanweb.github.io/general/registry/marxan.js"
TORNADO_PATH = "/marxan-server/"

class MarxanServer():
    def __init__(self, data):
        self.host = data['host']
        self.name = data['name']
        self.port = data['port']
        self.protocol = data['protocol']
        self.description = data['description']
        self.type = data['type']
        self.origin = data['origin']
        self.endpoint = data['endpoint']

    def authenticate(self, echo=True):
        #get the authenticate url
        authenticateUrl = self.endpoint + "validateUser?user=admin&password=password"
        #authenticate without checking SSL certificates
        try:
            r = requests.get(authenticateUrl, timeout=2, headers={'referer': self.origin}, verify=False)
            if (r.text.find('VFS connection does not exist')!=-1):
                raise RequestException("VFS connection does not exist")
            if ('error' in r.json()):
                raise Exception(r.json()['error'])
            self.cookies = r.cookies
            if echo:
                print("Authenticated")
        except (ConnectTimeout) as e:
            print("ConnectTimeout")
            raise
        except (ConnectionError) as e:
            print("ConnectionError")
            raise
        except (SSLError) as e:
            print("SSLError")
            raise
        except (RequestException) as e:
            print(e)
            raise
        except (Exception) as e:
            print(e)
            raise
        
    def makeRequest(self, url):
        r = requests.get(url, headers={'referer': self.origin}, cookies=self.cookies, verify=False)
        if ('error' in r.json()):
            raise Exception(r.json()['error'])
        return r.json()
    
    def addParameter(self, ConfigType, key, value):
        #get the request url
        url = self.endpoint + 'addParameter?type=' + ConfigType + '&key=' + key + ' &value=' + value
        #make the request
        response = self.makeRequest(url) 
        #print the results
        print("\n".join(response['info']))
        
    def getServerVersion(self):
        #get the request url
        response = self.makeRequest(self.endpoint + "getServerData") 
        #print the response
        print(response['serverData']['MARXAN_SERVER_VERSION'])
        
    def runSQL(self, fullfilename):
        filename = os.path.basename(fullfilename)
        #set the files dictionary and open the file in read binary mode
        files = {'value': open(fullfilename, 'rb')}
        #post the file
        r = requests.post(self.endpoint + 'uploadFileToFolder', headers={'referer': self.origin}, data={'filename': filename, 'destFolder':''}, files=files, cookies=self.cookies, verify=False)
        print(r.json()['info'])
        #execute the file
        response = self.makeRequest(self.endpoint + "runSQLFile?filename=" + filename)
        if (response['info']==0):
            print("Database update successful")
        else:
            print("Database update failed")
                
#helper for getting data from the marxan registry
class Registry():
    def __init__(self):
        r = requests.get(MARXAN_REGISTRY)
        #get the data
        data = r.text
        #get the marxan servers
        pos = data.find("MARXAN_SERVERS")
        if (pos == -1):
            raise Exception("MARXAN_SERVERS not found")
        startpos = data[pos:].find("[")
        if (startpos == -1):
            raise Exception("MARXAN_SERVERS starting array not found")
        endpos = data[pos:].find("]") + 1
        if (endpos == -1):
            raise Exception("MARXAN_SERVERS closing array not found")
        arrayStr = data[pos + startpos:pos + endpos].replace("'", '"')
        marxan_servers = json.loads(arrayStr)
        self.MarxanServers = []
        for server in marxan_servers:
            #requests to https://61c92e42cb1042699911c485c38d52ae.vfs.cloud9.eu-west-1.amazonaws.com:8081/ have to go to http://localhost:8081
            if server['host'] == '61c92e42cb1042699911c485c38d52ae.vfs.cloud9.eu-west-1.amazonaws.com':
                server['host'] = 'localhost'
                server['protocol'] = 'http:'
            server['origin'] = server['protocol'] + "//" + server['host'] + ":" + str(server['port'])
            server['endpoint'] = server['origin'] + TORNADO_PATH
            self.MarxanServers.append(MarxanServer(server))