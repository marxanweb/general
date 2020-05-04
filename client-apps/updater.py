#utiliy for updating all of the marxan servers from a single script
# either adds a new parameter to a *.dat file or updates an existing parameter value
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
        #print the response
        print(r.json()['info'])
        #get the update url
        # updateUrl = endpoint + "addParameter?type=user&key=SHOWWELCOMESCREEN&value=false"
        # updateUrl = endpoint + "addParameter?type=user&key=USEFEATURECOLORS&value=true"
        updateUrl = endpoint + "addParameter?type=project&key=NUMREPS&value=10"
        #run the update
        r2 = requests.get(updateUrl, headers={'referer': origin}, cookies=r.cookies, verify=False)
        if ('error' in r2.json()):
            raise Exception(r2.json()['error'])
        updates = r2.json()['info']
        print("\n".join(updates))
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
