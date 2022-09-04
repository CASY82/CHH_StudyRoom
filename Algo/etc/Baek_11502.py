import sys
import math

t = int(sys.stdin.readline())

prime = []

n = 1000

array = [True for i in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= n:
            array[i * j] = False
            j += 1

for i in range(2, n + 1):
    if array[i]:
        prime.append(i)

for _ in range(t):
    num = int(sys.stdin.readline())
    tmp = False

    for i in range(len(prime)):
        for j in range(len(prime)):
            for k in range(len(prime)):
                if prime[i] + prime[j] + prime[k] == num:
                    print(prime[i], prime[j], prime[k])
                    tmp = True

            if tmp:
                break

        if tmp:
            break

    if not tmp:
        print(0)