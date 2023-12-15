import hashlib
hasher = hashlib.md5()
with open('hash.py', 'rb') as afile:
    buf = afile.read()
    hasher.update(buf)
print(hasher.hexdigest())
