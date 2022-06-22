import sys

n = int(sys.stdin.readline())
cnt = 0

for i in range(1, n+1):
    tmp = list(str(i))
    tmp_sum = 0

    for j in tmp:
        tmp_sum += int(j)

    if i % tmp_sum == 0:
        cnt += 1

print(cnt)


#Python 통과 풀이
# total = 0
# n = int(input())
# k = {0:0}
# for i in range(1, n+1):
#     k[i] = (k[i//10] + i%10)
#     if not(i % k[i]):
#         total += 1
# print(total)