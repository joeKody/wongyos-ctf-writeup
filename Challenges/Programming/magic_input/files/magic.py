import hashlib
while True:
    a = float(input('enter a: '))
    b = float(input('enter b: '))
    if a > b:
        print('You Pass Level #1')
        if a * b < 0:
            print('You Pass Level #2')
            if a + b != a + b:
                print('You Pass Level #3')
                x = hashlib.md5(str(a / b).encode()).hexdigest()
                print('flag{' + x + '}')
                break
            else:
                print('You Fail Level #3')
        else:
            print('You Fail Level #2')
    else:
        print('You Fail Level #1')
