from django.conf import settings
from datetime import datetime
import base64
import json
import hmac
import hashlib

def defaultconverter(o):
    if isinstance(o, datetime):
        return o.__str__()

def decode_jwt(input):
    return base64.urlsafe_b64decode(input)

def base64url_encode(input):
    bytesString = input.encode('ascii')
    return base64.urlsafe_b64encode(bytesString).decode('utf-8')

def create_jwt(payload):
    header = {
        "alg":"HS256",
        "typ":"JWT",
    }

    secret_key = settings.SECRET_KEY
    total_params = str(base64url_encode(json.dumps(header))) + '.' + str(base64url_encode(json.dumps(payload, default=defaultconverter)))
    signature= hmac.new(secret_key.encode(), total_params.encode(), hashlib.sha256).hexdigest()
    token = total_params+'.'+str(base64url_encode(signature))
    return token