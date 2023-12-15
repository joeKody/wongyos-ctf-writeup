import hashlib
def call(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return call(n - 1) + call(n - 2)
n = int(open('call.txt').readline().strip())
x = int(input('x = '))
if call(x) == n:
    hasher = hashlib.md5(str(x).encode())
    print('flag{' + hasher.hexdigest() + '}')
else:
    print(call(x), 'incorrect')
