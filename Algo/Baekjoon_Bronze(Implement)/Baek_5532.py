l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

su = b // d
kuk = a // c

if b % d != 0:
    su += 1

if a % c != 0:
    kuk += 1

result = l - max(su, kuk)

print(result)