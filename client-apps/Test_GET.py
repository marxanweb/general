#test with
# python -W ignore Test_GET.py
import requests

DOMAIN = "https://andrewcottam.com:443"
#ENTER THE URL TO TEST HERE###########################################################################################
URL_TO_TEST = "wss://andrewcottam.com:443/marxan-server/getPUData?user=valeriepmculty&project=Test%20Project%20Val&puid=17917"

#authenticate
r = requests.get(DOMAIN + "/marxan-server/validateUser?user=admin&password=password", timeout=2, headers={'referer': DOMAIN}, verify=False)
#make the request
r2 = requests.get(DOMAIN + URL_TO_TEST, headers={'referer': DOMAIN}, cookies=r.cookies, verify=False)
print(r2.json())