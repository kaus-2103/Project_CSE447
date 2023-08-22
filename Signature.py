from Crypto.PublicKey import RSA

from hashlib import sha512
class Signature:
  def __init__(self):
    self.n = 0xf51518d30754430e4b89f828fd4f1a8e8f44dd10e0635c0e93b7c01802729a37e1dfc8848d7fbbdf2599830268d544c1ecab4f2b19b6164a4ac29c8b1a4ec6930047397d0bb93aa77ed0c2f5d5c90ff3d458755b2367b46cc5c0d83f8f8673ec85b0575b9d1cea2c35a0b881a6d007d95c1cc94892bec61c2e9ed1599c1e605f
    self.e = 0x10001
    self.d = 0x165ecc9b4689fc6ceb9c3658977686f8083fc2e5ed75644bb8540766a9a2884d1d82edac9bb5d312353e63e4ee68b913f264589f98833459a7a547e0b2900a33e71023c4dedb42875b2dfdf412881199a990dfb77c097ce71b9c8b8811480f1637b85900137231ab47a7e0cbecc0b011c2c341b6de2b2e9c24d455ccd1fc0c21
  def generation(self,message):

      hash = int.from_bytes(sha512(message).digest(), byteorder='big')
      signature = pow(hash, self.d, self.n)
      return hex(signature)
  def verification(self,cipher,signature):
      hash = int.from_bytes(sha512(cipher).digest(), byteorder='big')
      signature=int(signature,0)
      Signature = pow(cipher, self.e, self.n)
      if (hash == Signature):
        return f"Signature valid"
