import sys

n = int(sys.stdin.readline())

numer = 118

prime = [True] * (numer + 1)
cnt = 0
for i in range(2, int(numer ** 0.5)+1):
    if prime[i]:
        for j in range(i*i, numer+1, i):
            cnt += 1
            prime[j] = False

prime_num = []

for i in range(2, 119):
    if prime[i]:
        prime_num.append(i)

for _ in range(n):
    num = int(sys.stdin.readline())

    check = 0

    for fir in prime_num:
        for sec in prime_num:
            if num == fir + sec:
                check = True
                break

        if check:
            break

    if check:
        print("Yes")
    else:
        print("No")