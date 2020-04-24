#utiliy for updating all of the marxan servers from a single script
#run with:
# python3 -W ignore -m getServerVersions
import requests, json, OpenSSL
from requests.exceptions import ConnectTimeout, SSLError, RequestException, ConnectionError
from operator import itemgetter
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
    print(server['name'] , end=' ', flush=True)
    #get the length of the longest server text
    longest = sorted([len(m['name']) for m in marxan_servers])[-1]
    #pad to the same position
    print(((longest - len(server['name'])) + 5) * " ", end=' ', flush=True )
    try:
        #make the request to get the server data and turn off SSL certificate checking as there are some issues on marxantraining.org even though it works in a browser
        r = requests.get(endpoint + "getServerData", timeout=1, headers={'referer': origin}, verify=False)
        if (r.text.find('VFS connection does not exist')!=-1):
            raise RequestException("VFS connection does not exist")
        if ('error' in r.json()):
            raise Exception(r.json()['error'])
        #print the response
        print(r.json()['serverData']['MARXAN_SERVER_VERSION'])
    except (ConnectTimeout) as e:
        print("ConnectTimeout")
        pass
    except (ConnectionError) as e:
        print("ConnectionError")
        pass
    except (SSLError) as e:
        print("SSLError")
        pass
    except (RequestException) as e:
        print(e)
        pass
    except (Exception) as e:
        print(e)
        pass
