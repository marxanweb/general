import tornado, asyncio, json
from tornado import gen, websocket, httputil 
from tornado.httpclient import HTTPRequest, AsyncHTTPClient
#constants
LOGIN_USER = "admin"
LOGIN_PASSWORD = "password"
PROTOCOL = "https://"
DOMAIN = "andrewcottam.com"
PORT = '80' if PROTOCOL == "http://" else '443'
REFERER = PROTOCOL + DOMAIN + ":" + PORT
HTTP_ENDPOINT = REFERER + "/marxan-server/"
WS = "ws://" if PROTOCOL == "http://" else "wss://" 
WS_ENDPOINT = WS + DOMAIN + ":" + PORT + "/marxan-server/"
USER = "unit_tester"
PROJECT = "test_project"

#global variables
cookie = None

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

def getDictResponse(response):
    """
    Parses the response from either a GET/POST request or a WebSocket message to check for errors
    """
    #set a flag to indicate if the request is complete or not
    requestComplete = False
    if hasattr(response, 'body'):
        #for GET/POST requests there is only one response
        _dict = dict(json.loads(response.body.decode("utf-8"))) 
        requestComplete = True
    else:
        #for WebSocket requests there will be more than one message
        _dict = dict(json.loads(response)) 
        #if the status is Finished then the request is complete
        requestComplete = _dict['status'] == "Finished"
    #print any error messages
    if ('error' in _dict.keys()):
        err = _dict['error']
        #leave out the href link to the error message
        if err.find("See <")!=-1:
            err = err[:err.find("See <")]
        print(err, end=' ', flush=True)
    return _dict

async def makeRequest(url, **kwargs):
    #get any existing headers
    if "headers" in kwargs.keys():
        d1 = kwargs['headers']
    else:
        d1 = {}
    # get the generic headers
    d2 = {'Cookie': cookie, "referer": REFERER} if cookie else {"referer": REFERER}
    #merge the headers
    kwargs.update({'headers': {**d1, **d2}, 'validate_cert': False, 'request_timeout': None})
    #make the request
    http_client = AsyncHTTPClient()
    try:
        response = await http_client.fetch(HTTPRequest(HTTP_ENDPOINT + url, **kwargs))
    except Exception as e:
        print(e)
    else:
        #if the response has cookies then set them globally
        if ('set-cookie' in response.headers.keys() and response.headers['set-cookie']):
            setCookies(response)
        # get the response as a dictionary
        _dict = getDictResponse(response)
        print(_dict)
        return _dict

async def makeWebSocketRequest(request, **kwargs):
    msgs = []
    # add the cookies if they have been set
    if cookie:
        kwargs.update({'headers':{'Cookie': cookie, "referer": REFERER}})
    else:
        kwargs.update({'headers':{"referer": REFERER}})
    #dont attempt to validate the SSL certificate otherwise you get SSL errors - not sure why and set the request timeout (5 seconds by default)
    kwargs.update({'validate_cert': False, 'request_timeout': None})
    #make the request
    try:
        ws_client = await tornado.websocket.websocket_connect(HTTPRequest(WS_ENDPOINT + request, **kwargs))
    except Exception as e:
        print(e)
    else:
        #log the messages from the websocket
        print("\n")
        while True:
            msg = await ws_client.read_message()
            if not msg:
                break
            _dict = getDictResponse(msg)
            msgs.append(_dict)
            # print(_dict)
        return msgs

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(makeRequest('validateUser?user=' + LOGIN_USER + '&password=' + LOGIN_PASSWORD))
    asyncio.get_event_loop().run_until_complete(makeWebSocketRequest('createPlanningUnitGrid?iso3=AND&domain=Terrestrial&areakm2=50&shape=square'))