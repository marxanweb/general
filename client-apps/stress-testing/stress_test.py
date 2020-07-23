#
# Copyright (c) 2020 Andrew Cottam.
#
# This file is part of marxanweb/general
# (see https://github.com/marxanweb/general).
#
# License: European Union Public Licence V. 1.2, see https://opensource.org/licenses/EUPL-1.2
#
import tornado, asyncio, json, datetime, colorama, stress_test_jobs, uuid, urllib
from tornado import websocket, httputil, queues, gen
from tornado.httpclient import HTTPRequest, AsyncHTTPClient
from colorama import Fore, Back, Style

#constants
LIVE_OUTPUT = True
PROTOCOL = "https://"
# DOMAIN = "andrewcottam.com"
# DOMAIN = "marxantraining.org"
DOMAIN = "azure.marxanweb.org"
PORT = '80' if PROTOCOL == "http://" else '443'
REFERER = PROTOCOL + DOMAIN + ":" + PORT
HTTP_ENDPOINT = REFERER + "/marxan-server/"
WS = "ws://" if PROTOCOL == "http://" else "wss://"
WS_ENDPOINT = WS + DOMAIN + ":" + PORT + "/marxan-server/"
USER = "unit_tester"
PROJECT = "test_project"
CONCURRENT_TASKS = 1000
CURRENT_TEST = stress_test_jobs.JOB_20
CONCURRENT_USERS = 5

#global variables
adminUser = None

colorama.init()

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
        # print(Fore.RESET + timestamp() + str(request.user.id) + " " + request.url + 5*" " + json.dumps(_dict))
        pass
    if "error" in _dict.keys():
        print(Fore.RED+ timestamp() + _dict['error'])
    return _dict

def getRequestMethod(url):
    pos = url.find("?") if url.find("?") != -1 else len(url)
    return url[:pos]
    
def getElapsedTime(request):
    request.t2 = datetime.datetime.now()
    return request.t2 - request.t1
    
def logStart(request):
    request.t1 = datetime.datetime.now()
    if LIVE_OUTPUT:
        if request.user != None:
            print(Fore.GREEN + timestamp() + str(request.user.id) + " " + request.method)
        else:
            print(Fore.GREEN + timestamp() + request.method)
            
def logFinish(request):
    request.elapsed = getElapsedTime(request)
    if LIVE_OUTPUT:
        if request.user != None:
            print(Fore.BLUE + timestamp() + str(request.user.id) + " " + request.method + " (" + str(request.elapsed)[5:] + "s)") 
        else:
            print(Fore.BLUE + timestamp() + request.method + " (" + str(request.elapsed)[5:] + "s)")

#gets all of the requests for a user from the CURRENT_TEST suite
def getUserRequests(user):
    requests = []
    for request in CURRENT_TEST:
        #replace any place holders with the runtime data
        url = request[1].replace("USER", user.user)
        url = url.replace("PROJECT", "Start%20project")
        requests.append(Request(request[0], url, user))
    return requests
        
async def makeRequest(request, **kwargs):
    logStart(request)
    try:
        if request.type == "WebSocket":
            msgs = await makeWebSocketRequest(request, **kwargs)
            request.response = msgs
            logFinish(request)
            return msgs
        else:
            response, _dict = await makeHttpRequest(request, **kwargs)
            request.response = _dict
            logFinish(request)
            return response, _dict
    except Exception as e:
        request.elapsed = getElapsedTime(request)
        print(Fore.RED + timestamp() + str(request.user.id) + " " + request.method + " " + str(e) + " (" + str(request.elapsed)[5:] + "s)")

async def makeHttpRequest(request, **kwargs):
    #get any existing headers
    if "headers" in kwargs.keys():
        d1 = kwargs['headers']
    else:
        d1 = {}
    # get the generic headers
    d2 = {'Cookie': request.user.cookie, "referer": REFERER} if request.user else {"referer": REFERER}
    #merge the headers
    kwargs.update({'headers': {**d1, **d2}, 'validate_cert': False, 'request_timeout': None})
    #make the request
    http_client = AsyncHTTPClient()
    response = await http_client.fetch(HTTPRequest(HTTP_ENDPOINT + request.url, method=request.type, **kwargs))
    # get the response as a dictionary
    _dict = getDictResponse(request, response)
    return response, _dict

async def makeWebSocketRequest(request, **kwargs):
    msgs = []
    #dont attempt to validate the SSL certificate otherwise you get SSL errors - not sure why and set the request timeout (5 seconds by default)
    kwargs.update({'headers':{'Cookie': request.user.cookie, "referer": REFERER}, 'validate_cert': False, 'request_timeout': None})
    #make the request
    ws_client = await tornado.websocket.websocket_connect(HTTPRequest(WS_ENDPOINT + request.url, **kwargs))
    while True:
        msg = await ws_client.read_message()
        if not msg:
            break
        _dict = getDictResponse(request, msg)
        msgs.append(_dict)
    return msgs

async def stressTestServer(numUsers=1):
    async def worker():
        async for request in queue:
            if request is None:
                return
            if request.url in fetching:
                return
            fetching.add(request.url)
            try:
                #fetch the request
                await makeRequest(request)
                fetched.add(request.url)
            except Exception as e:
                print(Fore.BLUE + "Exception: %s %s" % (e, request))
                dead.add(request.url)
            finally:
                queue.task_done()
    #create an admin user to be able to add/remove users
    global adminUser
    adminUser = User()
    await adminUser.authenticate()
    #instantiate the user list
    users = []
    #instantiate the requests list
    requests = []
    for u in range(numUsers):
        #create a new user 
        user = User(u)
        await user.createUser()
        await user.authenticate()
        #get the requests to submit
        requests.extend(getUserRequests(user))
        users.append(user)
    #create a queue for the request to submit
    queue = queues.Queue()
    #initialise the sets to track progress
    fetching, fetched, dead = set(), set(), set()
    #add all the requests to the queue
    for _request in requests:
        await queue.put(_request)
    # Start workers, then wait for the work queue to be empty.
    workers = gen.multi([worker() for _ in range(CONCURRENT_TASKS)])
    await queue.join()
    assert fetching == (fetched | dead)
    # Signal all the workers to exit.
    for _ in range(CONCURRENT_TASKS):
        await queue.put(None)
    await workers
    # outputResults(user)
    #delete all users
    for user in users:
        await user.deleteUser()

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
    def __init__(self, type, url, user):
        self.type = type
        self.url = url
        self.response = None
        self.user = user
        self.method = getRequestMethod(url)

class User():
    def __init__(self, id=None):
        #if an id is passed then create a normal user
        if id != None:
            self.id = str(id).rjust(2,"0")
            self.user = "user_" + self.id
            self.password = uuid.uuid4().hex
        else: # otherwise create an admin user
            self.id = "admin"
            self.user = "admin"
            self.password = "password"

    def setCookie(self, response):
        #get the cookies
        cookies = response.headers['set-cookie'].split(",")
        parsed = [httputil.parse_cookie(c) for c in cookies]
        #get the user cookie
        userCookie = next((c for c in parsed if "user" in c.keys()), None)
        #get the role cookie
        roleCookie = next((c for c in parsed if "role" in c.keys()), None)
        self.cookie = "user=" + userCookie['user'] + ";role=" + roleCookie['role']

    async def createUser(self):
        body = urllib.parse.urlencode({"user":self.user,"password":self.password,"fullname":"wibble","email":"a@b.com"})
        response, _dict = await makeRequest(Request("POST", 'createUser', None), body=body)
        if "error" in _dict.keys():
            raise Exception(_dict['error'])

    async def authenticate(self):
        response, _dict = await makeRequest(Request("GET", 'validateUser?user=' + self.user + '&password=' + self.password, None))
        if "error" in _dict.keys():
            raise Exception("Authentication error")
        else:
            self.setCookie(response)
    
    async def deleteUser(self):
        response, _dict = await makeRequest(Request('GET','deleteUser?user=' + self.user, adminUser))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(stressTestServer(CONCURRENT_USERS))
