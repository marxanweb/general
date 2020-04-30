import tornado, asyncio, json, datetime, colorama, stressTestingJobs
from tornado import websocket, httputil, queues, gen
from tornado.httpclient import HTTPRequest, AsyncHTTPClient
from colorama import Fore, Back, Style

#constants
LIVE_OUTPUT = True
PROTOCOL = "https://"
DOMAIN = "andrewcottam.com"
# DOMAIN = "marxantraining.org"
# DOMAIN = "azure.marxanweb.org"
PORT = '80' if PROTOCOL == "http://" else '443'
REFERER = PROTOCOL + DOMAIN + ":" + PORT
HTTP_ENDPOINT = REFERER + "/marxan-server/"
WS = "ws://" if PROTOCOL == "http://" else "wss://" 
WS_ENDPOINT = WS + DOMAIN + ":" + PORT + "/marxan-server/"
USER = "unit_tester"
PROJECT = "test_project"
CONCURRENT_TASKS = 10

#global variables
current_test = stressTestingJobs.JOB_01
cookie = None
q = None

colorama.init()
def setCookies(response):
    #get the cookies
    cookies = response.headers['set-cookie'].split(",")
    parsed = [httputil.parse_cookie(c) for c in cookies]
    #get the user cookie
    userCookie = next((c for c in parsed if "user" in c.keys()), None)
    #get the role cookie
    roleCookie = next((c for c in parsed if "role" in c.keys()), None)
    global cookie
    cookie = "user=" + userCookie['user'] + ";role=" + roleCookie['role']

def timestamp():
    return datetime.datetime.now().strftime("%H:%M:%S.%f") + 5*" "
    
def getDictResponse(request, response):
    if hasattr(response, 'body'):
        #for GET/POST requests there is only one response
        _dict = dict(json.loads(response.body.decode("utf-8"))) 
    else:
        #for WebSocket requests there will be more than one message
        _dict = dict(json.loads(response)) 
    if LIVE_OUTPUT and 'status' in _dict.keys() and _dict['status'] != 'RunningMarxan':
        print(Fore.RESET + timestamp() + request.url + 5*" " + json.dumps(_dict))
        pass
    return _dict

def logStart(url):
    if LIVE_OUTPUT:
        print(Fore.GREEN + timestamp() + url)
    
def logFinish(url):
    if LIVE_OUTPUT:
        print(Fore.RED + timestamp() + url)
        
async def makeRequest(user, request, **kwargs):
    logStart(request.url)
    if request.type == "WebSocket":
        msgs = await makeWebSocketRequest(user, request, **kwargs)
        request.response = msgs
        logFinish(request.url)
        return msgs
    else:
        response, _dict = await makeHttpRequest(user, request, **kwargs)
        request.response = _dict
        logFinish(request.url)
        return response, _dict

async def makeHttpRequest(user, request, **kwargs):
    #get any existing headers
    if "headers" in kwargs.keys():
        d1 = kwargs['headers']
    else:
        d1 = {}
    # get the generic headers
    d2 = {'Cookie': user.cookie, "referer": REFERER} if user else {"referer": REFERER}
    #merge the headers
    kwargs.update({'headers': {**d1, **d2}, 'validate_cert': False, 'request_timeout': None})
    #make the request
    http_client = AsyncHTTPClient()
    try:
        response = await http_client.fetch(HTTPRequest(HTTP_ENDPOINT + request.url, **kwargs))
    except Exception as e:
        print(e)
    else:
        # get the response as a dictionary
        _dict = getDictResponse(request, response)
        return response, _dict
    
async def makeWebSocketRequest(user, request, **kwargs):
    msgs = []
    #dont attempt to validate the SSL certificate otherwise you get SSL errors - not sure why and set the request timeout (5 seconds by default)
    kwargs.update({'headers':{'Cookie': user.cookie, "referer": REFERER}, 'validate_cert': False, 'request_timeout': None})
    #make the request
    try:
        ws_client = await tornado.websocket.websocket_connect(HTTPRequest(WS_ENDPOINT + request.url, **kwargs))
    except Exception as e:
        print(e)
    else:
        while True:
            msg = await ws_client.read_message()
            if not msg:
                break
            _dict = getDictResponse(request, msg)
            msgs.append(_dict)
        return msgs

async def createRequestQueue():
    async def worker(user):
        async for request in q:
            if request is None:
                return
            if request.url in fetching:
                return
            fetching.add(request.url)
            try:
                #fetch the request
                await makeRequest(user, request)
                fetched.add(request.url)
            except Exception as e:
                log("Exception: %s %s" % (e, request))
                dead.add(request.url)
            finally:
                q.task_done()
    
    #create a new user and authenticate
    user = User("admin", "password")
    await user.authenticate()
    #get the request to submit
    user.requests = [Request(request[0], request[1]) for request in current_test]
    #create a queue for the request to submit
    global q
    q = queues.Queue()
    #initialise the sets to track progress
    fetching, fetched, dead = set(), set(), set()
    #add all the requests to the queue
    for _request in user.requests:
        await q.put(_request)
    # Start workers, then wait for the work queue to be empty.
    workers = gen.multi([worker(user) for _ in range(CONCURRENT_TASKS)])
    await q.join()
    assert fetching == (fetched | dead)
    # Signal all the workers to exit.
    for _ in range(CONCURRENT_TASKS):
        await q.put(None)
    await workers
    outputResults(user)

def outputResults(user):
    #get the longest request url length
    longest = sorted([len(r.url) for r in user.requests])[-1]
    for _request in user.requests:
        print(_request.url + (60-len(_request.url))*" ", end=' ', flush=True)        
        if type(_request.response) == dict:
            print(json.dumps(_request.response)[:80])
        else:
            if len(_request.response) > 0:
                print(json.dumps(_request.response[-1])[:80])
    print("Finished all requests")
        
class Request():
    def __init__(self, type, url):
        self.type = type
        self.url = url
        self.response = None
        
class User():
    def __init__(self, user, password):
        self.user = user
        self.password = password
    
    def setCookie(self, response):
        #get the cookies
        cookies = response.headers['set-cookie'].split(",")
        parsed = [httputil.parse_cookie(c) for c in cookies]
        #get the user cookie
        userCookie = next((c for c in parsed if "user" in c.keys()), None)
        #get the role cookie
        roleCookie = next((c for c in parsed if "role" in c.keys()), None)
        self.cookie = "user=" + userCookie['user'] + ";role=" + roleCookie['role']
    
    async def authenticate(self):
        response, _dict = await makeRequest(None, Request("GET", 'validateUser?user=' + self.user + '&password=' + self.password))
        if "error" in _dict.keys():
            raise Exception("Authentication error")
        else:
            self.setCookie(response)
    
if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(createRequestQueue())
    
