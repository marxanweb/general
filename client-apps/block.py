#utiliy for polling a server to check for blocking operations
import requests, json
from requests.exceptions import ConnectTimeout, SSLError, RequestException, ConnectionError
#ORIGIN = "https://61c92e42cb1042699911c485c38d52ae.vfs.cloud9.eu-west-1.amazonaws.com:8081"
ORIGIN = "http://18.200.163.92:8081" #public IP
TORNADO_PATH = "/marxan-server/"
ENDPOINT = ORIGIN + TORNADO_PATH

def blockMarxanServer(secs):
    #Disable security to run this
    try:
        #get the test url
        testUrl = ENDPOINT + "block?seconds=" + str(secs)
        #run the test
        r = requests.get(testUrl)
        if ('error' in r.json()):
            raise Exception(r.json()['error'])
        testResponse = r.json()['info']
        print(testResponse)
    except (ConnectTimeout) as e:
        print("ConnectTimeout")
    except (ConnectionError) as e:
        print("ConnectTimeout")
    except (SSLError) as e:
        print("SSLError")
    except (RequestException) as e:
        print(e)
    except (Exception) as e:
        print(e)
    finally:
        print("\n")

blockMarxanServer(10)