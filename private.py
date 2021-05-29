import base64
import hashlib
import hmac
import time



api_url = "https://api.kraken.com/"
private = "0/private/"

api_secret = base64.b64decode(API_PRIVATE_KEY)
api_path = api_url + private + "TradeBalance"
api_nonce = str(int(time.time()*1000))
api_post = "nonce=" + api_nonce + "&asset=xbt"

api_sha256 = hashlib.sha256(api_nonce + api_post).digest()
api_hmac = hmac.new(api_secret, api_path.encode() + api_sha256, hashlib.sha512)

api_signature = base64.b64encode(api_hmac.digest())

print(api_signature)

