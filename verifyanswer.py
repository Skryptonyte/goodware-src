"""
from Crypto.Util.number import *
from Crypto.Cipher import AES



cipher = AES.new(b"niteveryevilkeys",AES.MODE_ECB)

s = open("flag.enc","rb").read()
s += b'\x00' * (16 - len(s)%16)
#s = b''.join([s[i:i+16][::-1] for i in range(0,len(s),16)])
enc = cipher.decrypt(s)

print(enc)
"""

from aes import AES
import Crypto.Cipher.AES


c = AES(b"niteveryevilkeys")
s = open("flag.enc","rb").read()


print("Modified AES Test:")
print(c.decrypt_cbc(s,b'veryevilinitvect'))


print("pycryptodome AES test (This shouldn't work!)")
cipher = Crypto.Cipher.AES.new(b"niteveryevilkeys",Crypto.Cipher.AES.MODE_CBC,iv=b'veryevilinitvect')
print(cipher.decrypt(s))