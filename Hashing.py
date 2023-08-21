import hashlib

class Hash:
    def __init__(self) -> None:
        pass
    def SHA1(self, plaintext ):
        plaintext = plaintext.strip().encode('utf-8')
        ciphertext = hashlib.sha1(plaintext).hexdigest()

        return ciphertext
    def SHA256(self, plaintext):
        plaintext = plaintext.strip().encode('utf-8')
        ciphertext = hashlib.sha256(plaintext).hexdigest()

        return ciphertext

    def MD5(self, plaintext):
        plaintext = plaintext.strip().encode('utf-8')
        ciphertext = hashlib.md5(plaintext).hexdigest()

        return ciphertext
test = Hash()
# print(test.SHA1('Fuad pocha'))
# print(test.SHA256('Fuad pocha'))