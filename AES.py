from hashlib import md5
from base64 import b64decode
from base64 import b64encode

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad


class AESCipher:
    def __init__(self, key):
        self.key = md5(key.encode('utf8')).digest()

    def encryptCBC(self, data):
        iv = get_random_bytes(AES.block_size)
        self.cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'), 
            AES.block_size)))

    def decryptCBC(self, data):
        raw = b64decode(data)
        self.cipher = AES.new(self.key, AES.MODE_CBC, raw[:AES.block_size])
        return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)
    
    def encryptECB(self,data):
        iv = get_random_bytes(AES.block_size)
        self.cipher = AES.new(self.key, AES.MODE_ECB, iv)
        return b64encode(iv + self.cipher.encrypt(pad(data.encode('utf-8'), 
            AES.block_size)))
    
    def decryptEBC(self,data):
        raw = b64decode(data)
        self.cipher = AES.new(self.key,AES.MODE_ECB,raw[:AES.block_size])
        return unpad(self.cipher.decrypt(raw[AES.block_size:]), AES.block_size)
    

# if __name__ == '__main__':
#     print('TESTING ENCRYPTION')
#     msg = input('Message...: ')
#     pwd = input('Password..: ')
#     print('Ciphertext:', AESCipher(pwd).encrypt(msg).decode('utf-8'))

#     print('\nTESTING DECRYPTION')
#     cte = input('Ciphertext: ')
#     pwd = input('Password..: ')
#     print('Message...:', AESCipher(pwd).decrypt(cte).decode('utf-8'))