import sys

a, b, c = map(int, sys.stdin.readline().split())

odd_res = a ^ b
even_res = a ^ b ^ b

if c % 2 == 0:
    print(even_res)
else:
    print(odd_res)