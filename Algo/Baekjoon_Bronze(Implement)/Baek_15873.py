import sys

num = sys.stdin.readline().strip()

if len(num) == 2:
    num = int(num)
    print(num // 10 + num % 10)
elif len(num) <= 3 and num[1] == '0':
    num = int(num)
    print(num//10 + num%10)
else:
    num = int(num)
    print(num//100 + num%100)