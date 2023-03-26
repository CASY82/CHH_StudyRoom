import sys

n, x = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

end = 0
loc_sum = 0
result = 0
count = 0

for start in range(n):
    while abs(end - start) < x and end < n:
        loc_sum += num[end]
        end += 1

    if loc_sum > result:
        result = loc_sum
    loc_sum -= num[start]

end = 0
loc_sum = 0

for start in range(n):
    while abs(end - start) < x and end < n:
        loc_sum += num[end]
        end += 1

    if loc_sum == result:
        count += 1
    loc_sum -= num[start]

if result > 0:
    print(result)
    print(count)
else:
    print("SAD")

#뭔가 짧게 할 수 있었을거 같아서 찾아본 다른 사람 정답

# N,X = map(int,input().split())
#
# visit = list(map(int,input().split()))
#
# result = sum(visit[:X])
# tmp = result
# r_c = 1
# for i in range(X,N):
#     tmp += visit[i]
#     tmp -= visit[i-X]
#     if tmp == result:
#         r_c += 1
#     elif tmp > result:
#         result = tmp
#         r_c = 1
# if result != 0:
#     print(result)
#     print(r_c)
# else:
#     print("SAD")
