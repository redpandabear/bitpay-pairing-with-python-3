import bitpay.key_utils as key_utils
from bitpay.client import Client

with open("keys/local.pem", 'r') as f:
    key = f.read()
client = Client(api_uri="https://bitpay.com", insecure=False, pem=key, tokens={})
token = client.create_merchant_token()
print(token)
# This should print something like the following:
# {'data': [{'policies': [{'policy': 'id', 'method': 'inactive', 'params': ['Txxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx']}], 'token': 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx', 'facade': 'merchant', 'dateCreated': 1490000000000, 'pairingExpiration': 1490000000000, 'pairingCode': 'xxxxxxx'}]}
with open("tokens/local.txt", 'w') as f:
    f.write(str(token))