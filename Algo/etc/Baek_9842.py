import sys

n = int(sys.stdin.readline())

numer = 110000
prime = [True] * (numer+1)
prime_num = []

for i in range(2, int(numer ** 0.5)+1):
    if prime[i]:
        for j in range(i*i, numer+1, i):
            prime[j] = False

for i in range(1, numer):
    if prime[i]:
        prime_num.append(i)

print(prime_num[n])