import time
import hmac
import base64
import hashlib
import requests
import urllib


API_KEY = "PUBLIC_KEY"
SECRET_KEY = "SECRET_KEY"
CLIENT_NAME = "YOUR CLIENT NAME"

params = {
    "_input": "weth",
    "output": "usdc",
    "amount": 10,
    "chunks": 5
}
headers = {
    "CLIENT_NAME": CLIENT_NAME,
    "TIME": str(int(time.time())),
    "API_KEY": API_KEY
}

sorted_params = sorted(
    params.items(), key=lambda d: d[0], reverse=False)
encode_params = urllib.parse.urlencode(sorted_params)
sign_msg = ",".join([headers["API_KEY"], str(headers["TIME"]), encode_params])
sign = base64.b64encode(hmac.new(
    SECRET_KEY.encode("UTF-8"),
    sign_msg.encode("UTF-8"),
    digestmod=hashlib.sha256
).digest()).decode()
headers["SIGNATURE"] = sign

resp = requests.get("http://$ONEBIT_HOST/getQuote", params=params, headers=headers)
print(resp.json())
