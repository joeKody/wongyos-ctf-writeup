def encrypt(flag, n):
    enc = ''
    for c in flag:
        enc += hex(ord(c) + n)[2:]
        n += 1
    return enc

flag = input('Flag: ')
enc = encrypt(flag, 145)
open('enc.txt', 'w').write(enc)
 
