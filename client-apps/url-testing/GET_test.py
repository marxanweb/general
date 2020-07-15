#test with
# python -W ignore GET_test.py
import requests
from urllib.parse import urlparse

#ENTER THE URL TO TEST HERE###########################################################################################
TEST_URL = "https://andrewcottam.com/marxan-server/getPUData?user=valeriepmculty&project=Test%20Project%20Val&puid=17917"
# TEST_URL = "http://localhost:8081/marxan-server/addParameter?type=server&key=ENABLE_RESET&value=false"
# TEST_URL = "http://localhost:8081/marxan-server/getProject?user=admin&project=Coral%20Triangle%20Case%20Study"

#authenticate
parsed = urlparse(TEST_URL)
domain = parsed.scheme + "://" + parsed.netloc
print(domain)
r = requests.get(domain + "/marxan-server/validateUser?user=admin&password=password", timeout=2, headers={'referer': domain}, verify=False)
#make the request
r2 = requests.get(TEST_URL, headers={'referer': domain}, cookies=r.cookies, verify=False)
print(r2.json())