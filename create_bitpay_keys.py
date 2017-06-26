import bitpay.key_utils as key_utils

pem = key_utils.generate_pem()
with open("keys/local.pem", 'w') as f:
    f.write(pem)
sin = key_utils.get_sin_from_pem(pem)
print("Printing SIN")
print(sin)