#test
a, b = input().split()

a = ord(a)
b = ord(b)

if a < b:
    for i in range(a, b+1):
        print(chr(i), end=' ')
else:
    for i in range(b, a+1):
        print(chr(i), end=' ')