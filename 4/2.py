"""
jak szybko jestem wygenerowac w stanie 5000 hashy w md5 i crypt

5000 przez ten czas to bedzie wydajnosc
"""
import time
import crypt
from hashlib import md5


reps = 5000
password = 'ala'
salt = 'ala'
start = time.time()
for i in range(reps):
    hash = crypt.crypt(password, salt)
end = time.time()
dur = end - start
res = reps / dur
print('crypt: {}'.format(res))

start = time.time()
for i in range(reps):
    hash = md5(b'ala')
end = time.time()
dur = end - start
res = reps / dur
print('md5:   {}'.format(res))
