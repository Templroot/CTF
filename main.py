import hashlib


to_hash = 'LsBa$e64'
hash_object = hashlib.md5(str(to_hash).encode('utf-8'))
print('Hash :', hash_object.hexdigest())


# from stegano import lsb
#
# secret = lsb.hide("Linux.png", "Your key : enNzb2lie0xpbnV4X0hhc2hfTFNCfQ==\n")
# secret.save("Linux.png")
#
# show = lsb.reveal("Linux.png", encoding= "UTF-8")
# print(str(show

import base64

# import base64
# encoded = base64.b64encode(b'zssoib{Linux_Hash_LSB}')
# print (str(encoded))
#
# a = 'enNzb2lie0xpbnV4X0hhc2hfTFNCfQ=='
# print(str(base64.b64decode(a)))