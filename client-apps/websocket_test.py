#test with
# python -W ignore websocket_test.py
import asyncio, requests, tornado, json
from tornado.httpclient import HTTPRequest, AsyncHTTPClient
from tornado import websocket
from urllib.parse import urlparse

#ENTER THE URL TO TEST HERE###########################################################################################
TEST_URL = "wss://andrewcottam.com:443/marxan-server/preprocessFeature?user=steveschill&project=British%20Columbia%20Marine%20Case%20Study&planning_grid_name=pu_89979654c5d044baa27b6008f9d06&feature_class_name=f_9ef0acbea19b4f26b1c540b9b39e90&alias=BC:%200-20m%20Hard%20substrate&id=35132"

async def test_websocket():
    parsed = urlparse(TEST_URL)
    domain = "https://" + parsed.netloc if TEST_URL[:3] == "wss" else "http://" + parsed.netloc
    #create an admin user to be able to authenticate as admin
    r = requests.get(domain + "/marxan-server/validateUser?user=admin&password=password", timeout=2, headers={'referer': domain}, verify=False)
    #get the cookies
    for c in r.cookies:
        if c.name == 'role':
            role = c.value[1:-1]
        if c.name == 'user':
            user = c.value[1:-1]
    kwargs = {'headers':{'Cookie': 'user=' + user + ';role=' + role, "referer": domain}, 'validate_cert': False}
    #make the websocket request
    ws_client = await tornado.websocket.websocket_connect(HTTPRequest(TEST_URL, **kwargs))
    while True:
        msg = await ws_client.read_message()
        if not msg:
            break
        _dict = dict(json.loads(msg))
        print(_dict)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(test_websocket())
