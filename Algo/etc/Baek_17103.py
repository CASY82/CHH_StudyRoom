import sys

t = int(sys.stdin.readline())

max_num = 1000000
prime = []
prime_check = [True] * (max_num+1)

for i in range(2, int(max_num ** 0.5)+1):
    if prime_check[i]:
        for j in range(i*i, max_num+1, i):
            prime_check[j] = False

for pr in range(2, len(prime_check)):
    if prime_check[pr]:
        prime.append(pr)

for _ in range(t):
    n = int(sys.stdin.readline())

    cnt = 0
    prime_set = set(prime)

    for i in range(len(prime)):
        if prime[i] > n:
            break

        if n - prime[i] in prime_set:
            if n - prime[i] == prime[i]:
                prime_set.remove(prime[i])
            else:
                prime_set.remove(prime[i])
                prime_set.remove(n - prime[i])
            cnt += 1

    print(cnt)

# 나와 다른 풀이 참고 소스

# n = int(input())
# li = [int(input()) for _ in range(n)]
#
# prime = []
# check = [1]*1000001
# check[0] = 0
# check[1] = 0
# for i in range(2, 1000001):
#     if check[i] == 1:
#         prime.append(i)
#         for j in range(2*i, 1000001, i):
#             check[j]=0
#
# for num in li:
#     cnt=0
#     for item in prime:
#         if item>=num: break
#         elif check[num-item] and item<=num-item: cnt+=1
#     print(cnt)