import bitpay.key_utils as key_utils
from bitpay.client import Client

with open("keys/local.pem", 'r') as f:
    key = f.read()
client = Client(api_uri="https://bitpay.com", insecure=False, pem=key, tokens={})