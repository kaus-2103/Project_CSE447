from math import gcd

class RSACipher:
    def __init__(self,p,q) -> None:
        self.n = p * q

        phi = (p - 1) * (q - 1)

        for i in range(2, phi):
            if gcd(i, phi) == 1:
                e = i
                break
        self.e = e
        
        j = 0
        while True:
            if (j * e) % phi == 1:
                d = j
                break
            j += 1
        self.d = d

    def RSAencrypt(self,message):
        ct = (message ** self.e) % self.n
        # print(f"Encrypted message is {ct}")
        return f"Encrypted message is {ct}"

    
    def RSAdecrypt(self,ct):
        mes = (ct ** self.d) % self.n
        # print(f"Decrypted message is {mes}")
        return f"Decrypted message is {mes}"


# RSA(p=53, q=59, message=89)

# RSA(p=3, q=7, message=12)
# print(RSACipher(3,7).RSAencrypt(12))
# print(RSACipher(3,7).RSAdecrypt(3))