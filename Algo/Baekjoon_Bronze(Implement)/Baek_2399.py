# 시간 초과 pypy3로 해서 품
# import sys
#
# n = int(sys.stdin.readline().rstrip())
# num_array = list(map(int, sys.stdin.readline().rstrip().split()))
#
# sum_num = 0
#
# for i in range(n):
#     for j in range(i + 1, n):
#         sum_num += abs(num_array[i] - num_array[j])
#
# print(sum_num * 2)

# 파이썬에서는 수학 공식을 활용해 푼다.
n = int(input())
x = sorted(list(map(int, input().split())))
result = 0
for i in range(n):
    result += x[i] * 2 * (2 * i - n + 1)
print(result)
