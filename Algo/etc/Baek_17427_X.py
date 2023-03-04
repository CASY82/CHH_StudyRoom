import sys

num = int(sys.stdin.readline())

# 수학 문제였다.
# n 까지의 수에서 k 약수로 표현할 수 있는 갯수가 n//k
# 예를 들어 다음과 같다.
# f(1) = 1
# f(2) = 1 + 2
# f(3) = 1 + 3
# f(4) = 1 + 2 + 4
# g(4) = 1*4 + 2*2 + 3*1 + 4*1

print(sum((k*(num//k) for k in range(1, num+1))))