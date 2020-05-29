#utiliy for updating all of the marxan servers databases from a single script
import requests, json
from requests.exceptions import ConnectTimeout, SSLError, RequestException, ConnectionError
MARXAN_REGISTRY = "https://marxanweb.github.io/general/registry/marxan.js"
TORNADO_PATH = "/marxan-server/"
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
for server in marxan_servers:
    #get the request url
    origin = server['protocol'] + "//" + server['host'] + ":" + str(server['port'])
    #requests to https://61c92e42cb1042699911c485c38d52ae.vfs.cloud9.eu-west-1.amazonaws.com:8081/ have to go to http://localhost:8081
    if server['host'] == '61c92e42cb1042699911c485c38d52ae.vfs.cloud9.eu-west-1.amazonaws.com':
        origin = 'http://localhost:8081'
    endpoint = origin + TORNADO_PATH
    #the user/password are hardcoded for now
    authenticateUrl = endpoint + "validateUser?user=admin&password=password"
    print("------------------------------------")
    print("Updating: '" + server['name'] + "'")
    try:
        #authenticate to the server
        r = requests.get(authenticateUrl, timeout=2, headers={'referer': origin}, verify=False)
        if (r.text.find('VFS connection does not exist')!=-1):
            raise RequestException("VFS connection does not exist")
        if ('error' in r.json()):
            raise Exception(r.json()['error'])
        #upload the file
        FILENAME = 'update.sql'
        FULL_FILENAME = '/home/ubuntu/environment/marxanweb/general/client-apps/' + FILENAME
        #set the files dictionary and open the file in read binary mode
        files = {'value': open(FULL_FILENAME, 'rb')}
        #post the file
        r2 = requests.post(endpoint + 'uploadFileToFolder', headers={'referer': origin}, data={'filename': FILENAME,'destFolder':''}, files=files, cookies=r.cookies, verify=False)
        print(r2.json()['info'])
        #execute the file
        #get the endpoint
        url = endpoint + "runSQLFile?filename=" + FILENAME
        #make the request
        r2 = requests.get(url, headers={'referer': origin}, cookies=r.cookies, verify=False)
        if ('error' in r2.json()):
            raise Exception(r2.json()['error'])
        print(r2.json()['info'])
        
    except (ConnectTimeout) as e:
        print(e)
    except (ConnectionError) as e:
        print(e)
    except (SSLError) as e:
        print("SSLError")
    except (RequestException) as e:
        print(e)
    except (Exception) as e:
        print(e)
    finally:
        print("\n")
