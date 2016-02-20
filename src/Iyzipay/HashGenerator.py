import base64
import hashlib
import sys
from importlib import reload

reload(sys)


class HashGenerator:
    @staticmethod
    def generate_hash(api_key, secret_key, random_string, request):
        hash_str = api_key + random_string + secret_key + request.to_pki_request_string()
        hex_dig = hashlib.sha1(hash_str.encode()).digest()
        return base64.b64encode(hex_dig)
