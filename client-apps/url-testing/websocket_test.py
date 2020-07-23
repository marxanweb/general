#
# Copyright (c) 2020 Andrew Cottam.
#
# This file is part of marxanweb/general
# (see https://github.com/marxanweb/general).
#
# License: European Union Public Licence V. 1.2, see https://opensource.org/licenses/EUPL-1.2
#
#test with the following
# python -W ignore websocket_test.py
import asyncio, requests, tornado, json
from tornado.httpclient import HTTPRequest
from tornado import websocket
from urllib.parse import urlparse

#ENTER THE URL TO TEST HERE###########################################################################################
# TEST_URL = "wss://andrewcottam.com:443/marxan-server/preprocessFeature?user=steveschill&project=British%20Columbia%20Marine%20Case%20Study&planning_grid_name=pu_89979654c5d044baa27b6008f9d06&feature_class_name=f_9ef0acbea19b4f26b1c540b9b39e90&alias=BC:%200-20m%20Hard%20substrate&id=35132"
# TEST_URL = "ws://localhost:8081/marxan-server/createFeaturesFromWFS?wfsendpoint=https%3A%2F%2Fdservices2.arcgis.com%2F7p8XMQ9sy7kJZN4K%2Farcgis%2Fservices%2FCranes_Species_Ranges%2FWFSServer%3Fservice%3Dwfs%26request%3Dgetcapabilities&featuretype=Cranes_Species_Ranges%3ABlack_Crowned_Cranes&name=test&description=wibble"
TEST_URL = "wss://azure.marxanweb.org/marxan-server/runMarxan?user=admin&project=Fiji%20NBSAP" #doesnt finish in the client!!!
# TEST_URL = "wss://andrewcottam.com/marxan-server/runMarxan?user=admin&project=Fiji%20NBSAP" #does finish!!

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
    try:
        ws_client = await tornado.websocket.websocket_connect(HTTPRequest(TEST_URL, **kwargs))
        while True:
            msg = await ws_client.read_message()
            if not msg:
                break
            _dict = dict(json.loads(msg))
            print(_dict)
    finally:
        if not ws_client.close_code:
            print("The server closed the connection unexpectedly")

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(test_websocket())
