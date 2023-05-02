import sys

q = int(sys.stdin.readline())

for _ in range(q):
    num = int(sys.stdin.readline())

    binary_num = bin(num)[2:]
    if binary_num.count('1') == 1:
        print(1)
    else:
        print(0)

# 더 빠른 다른 사람 풀이
# import sys
# t=int(input())
# for _ in range(t):
#     a=int(sys.stdin.readline().rstrip())
#     if a&(-a)==a: print(1)
#     else: print(0)