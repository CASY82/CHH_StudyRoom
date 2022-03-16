import sys

MAX_NUM = 1000001
prime = [True] * MAX_NUM
prime_num = []
for i in range(2, int((MAX_NUM) ** 0.5) + 1):
    if prime[i]:
        for j in range(i*i, MAX_NUM, i):
            prime[j] = False

for i in range(2, MAX_NUM):
    if prime[i]:
        prime_num.append(i)

set_prime_num = set(prime_num)

while True:
    num = int(sys.stdin.readline())

    if num == 0:
        break

    a = 0
    b = 0

    for prime_odd in prime_num:
        if num - prime_odd in set_prime_num:
            a = prime_odd
            b = num - prime_odd
            check = True
            break

    if a == b == 0:
        print("Goldbach's conjecture is wrong.")
    else:
        print(num, "=", a, "+", b)
