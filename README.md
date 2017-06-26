# bitpay-pairing-with-python-3
This repository is used for pairing local keys on a machine with your bitpay account.

1. Install Python 3
2. Install pip3 for python 3.0+
3. In a terminal window type in "pip3 install ecdsa"
4. Run create_bitpay_keys.py using Python 3
    4a. A key will now be created in <PROJECT_ROOT>/keys/local.txt
5. Run pair_with_bitpay_using_keys.py using Python 3
    5a. A token will now be created in <PROJECT_ROOT>/tokens/local.txt