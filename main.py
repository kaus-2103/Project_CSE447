from AES import AESCipher
from RSA import RSACipher
from Hashing import Hash
from Signature import generation
from Signature import verification
from MAC import MAC


ask = str(input("What Encryption you want to use? \n >"))

if ask == 'AES':
    ask2 = str(input("What kind of mode do you want ? \n >"))
    if ask2 == 'CBC':
        ask3 = str(input("Do you want Encryption or Decryption ? \n >"))
        if ask3 == 'enc':
            plaintext = str(input("Give me your plaintext: \n >"))
            key = str(input("Give me your key: \n >"))
            print(AESCipher(key).encryptCBC(plaintext).decode("utf-8"))
        else:
            ciphertext = str(input("Give me your ciphertext: \n >"))
    elif ask2 == 'EBC':
        ask3 = str(input("Do you want Encryption or Decryption ? \n >"))
        if ask3 == 'enc':
            plaintext = str(input("Give me your plaintext: \n >"))
            key = str(input("Give me your key: \n >"))
            print(AESCipher(key).encryptCBC(plaintext).decode("utf-8"))
        else:
            ciphertext = str(input("Give me your ciphertext: \n >"))


elif ask =='RSA':
    ask3 = str(input("Do you want Encryption or Decryption ? \n >"))
    if ask3 == 'enc':
        p = int(input("Give me value of P: \n >"))
        q = int(input("Give me value of Q: \n >"))
        plaintext = int(input("Give me your plaintext: \n >"))
        print(RSACipher(p,q).RSAencrypt(plaintext))
    else:
        p = int(input("Give me value of P: \n >"))
        q = int(input("Give me value of Q: \n >"))
        ciphertext = int(input("Give me your ciphertext: \n >"))
        print(RSACipher(p,q).RSAdecrypt(ciphertext))



elif ask == 'Hash':
    ask2 = str(input('What kind of mode do you want ? \n >'))
    if ask2 == 'SHA1':
        plaintext = str(input("Give me your plaintext: \n >"))
        print(Hash().SHA1(plaintext))

    elif ask2 == "SHA256":
        plaintext = str(input("Give me your plaintext: \n >"))
        print(Hash().SHA256(plaintext))

    elif ask2 == "MD5":
        plaintext = str(input("Give me your plaintext: \n >"))
        print(Hash().MD5(plaintext))



elif ask=='Signature':
    ask2 = str(input('Do you want Generation or Verification ? \n >'))
    if ask2 == 'gen':
        plaintext = str(input("Give me your plaintext: \n >"))

        print(generation(plaintext,p=int(input("Give me value of P: \n >")),q=int(input("Give me value of Q: \n >"))))
    else:
       print(verification(num=int(input("Give me your ciphertext: \n >")),p=int(input("Give me value of P: \n >")),q=int(input("Give me value of Q: \n >"))))

elif ask=="MAC":
    plaintext = str(input('Give me your message: \n >'))
    print(MAC(plaintext))




