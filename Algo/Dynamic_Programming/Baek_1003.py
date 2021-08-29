# DP로 풀어보았다. 3번만에 통과!

import sys
t = int(sys.stdin.readline())

def fibonacci(n, zero, one, mem):
    if n == 0:
        zero[n] = 1
        return 0
    elif n == 1:
        one[n] = 1
        return 1

    if mem[n] != 0:
        return mem[n]


    mem[n] = fibonacci(n - 1, zero, one, mem) + fibonacci(n - 2, zero, one, mem)
    zero[n] = zero[n - 2] + zero[n - 1]
    one[n] = one[n - 2] + one[n - 1]
    return mem[n]


for i in range(t):
    zero_count = [0] * 41
    one_count = [0] * 41
    memoize = [0] * 41

    n = int(sys.stdin.readline())

    fibonacci(n, zero_count, one_count, memoize)

    print(zero_count[n], one_count[n], end=' ')

# 원래의 피보나치

# def fibonacci(n):
#     if n == 0:
#         print('0')
#         return 0
#     elif n == 1:
#         print('1')
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)
#
#
# print(fibonacci(int(input())))

# 다른 사람 풀이 (내 풀이와 비교하니, 불필요한 부분이 발견되었다. 굳이 피보나치 결과는 저장할 필요도 없고 구할 필요도 없어서 빼도됨)

# import sys
# T = int(sys.stdin.readline())
#
# for _ in range(T):
#     N = int(sys.stdin.readline())
#     if N == 0:
#         print(1, 0)
#     elif N == 1:
#         print(0, 1)
#     else:
#         a, b = 0, 1
#         for _ in range(N-1):
#             a, b = b, a + b
#         print(a, b)

# 굳이 동적 프로그래밍 방법을 사용하지 않아도 풀 수 있었다. 라는 사실...
# l = [0,1]
# for i in range(40):
#     l.append(l[i]+l[i+1])
# for i in range(int(input())):
# 	g = int(input())
# 	if g==0: print('1 0')
# 	else: print(str(l[g-1]),str(l[g]))