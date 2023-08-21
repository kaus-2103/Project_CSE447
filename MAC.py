import os
# import sys
import binascii
# import hashlib


from cryptography.hazmat.primitives import cmac
from cryptography.hazmat.primitives.ciphers import algorithms

def MAC(subject):
    message=subject.encode()
    key = os.urandom(16)
    c_obj = cmac.CMAC(algorithms.TripleDES(key))
    c_obj.update(message)
 
    signature = c_obj.finalize()
    return binascii.b2a_hex(signature).decode()

# print(MAC(subject='Iambatmanakjfasdhbfjhasdgf asdyfgasdfasdfiausgd asgdfhbas'))