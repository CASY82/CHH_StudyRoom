#시간이 초과합니다.(pypy3로 하면 통과;;;)

T = int(input())
num_list = []
result = [0 for _ in range(T)]
data = 0

for i in range(T):
    a, b = map(int, input().split())

    data = 1

    for _ in range(b):
        data = (data * a) % 10

    if data == 0:
        data = 10

    result[i] = data

for i in range(T):
    print(result[i])


#왜 틀리는 걸까?(반례를 못찾음...)
# T = int(input())
# result = []
# d = 0
#
# for i in range(T):
#     a, b = map(int, input().split())
#
#     d = a % 10
#
#     if d == 1 or d == 5 or d == 6:
#         result.append(a % 10)
#     elif d == 2 or d == 3 or d == 7 or d == 8:
#         quota = b % 4
#         result.append((a ** quota) % 10)
#     elif d == 4 or d == 9:
#         quota = b % 2
#         result.append((a ** quota) % 10)
#     else:
#         result.append(10)
#
#
# for i in range(len(result)):
#      print(result[i])