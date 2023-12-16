import random

def func1(n):
    x = 1
    for i in range(n):
        x = x * (i + 1)
    return x

def func2(n):
    x = 1
    for i in range(n):
        x = x * 2
    return x

def func3(n):
    x = 0
    for i in range(n, 0, -1):
        x = x + i
    return x

def func4(n):
    x = 0
    for i in range(n):
        x = x + n
    return x

flag = input('Enter Flag: ')
enc = []
for char in flag:
    i = random.randint(1, 4)
    if i == 1:
        enc.append(func1(ord(char)))
    elif i == 2:
        enc.append(func2(ord(char)))
    elif i == 3:
        enc.append(func3(ord(char)))
    else:
        enc.append(func4(ord(char)))
print(enc)
