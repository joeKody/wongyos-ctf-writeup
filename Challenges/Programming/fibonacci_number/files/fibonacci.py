import hashlib
def fibonacci(n):
    #fibonacci(0) = 0
    #fibonacci(1) = 1
    #fibonacci(2) = fibonacci(1) + fibonacci(0)
    #fibonacci(3) = fibonacci(2) + fibonacci(1)
    #fibonacci(4) = fibonacci(3) + fibonacci(2)
    #fibonacci(5) = fibonacci(4) + fibonacci(3)
    #fibonacci(n) = fibonacci(n - 1) + fibonacci(n - 2)
    return 0

n = int(input('Enter n: '))
key = '9809463517264670023038788649658295091956272699959366635620342487725314342549664567'
if str(fibonacci(n)) == key:
    string = hashlib.md5(str(n + 19).encode('utf-8')).hexdigest()
    print(chr(102) + chr(108) + chr(97) + chr(103) + chr(123) + string + chr(125))
else:
    print('try again')
