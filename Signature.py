from Hashing import Hash
from RSA import RSACipher

def generation(message,p,q):
    message = Hash().SHA256(message)
    print(message,"message")
    num = int(message,16)
    print(num,"num")
    return RSACipher(p,q).RSAencrypt(num)

def verification(num,p,q):
    num = int(RSACipher(p,q).RSAdecrypt(num))
    
    message = hex(num)[2:]

    return message
    


# print(generation('iambatman',3,7))
# print(verification(0,3,7))
