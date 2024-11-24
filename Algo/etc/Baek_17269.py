import sys

n, m = map(int, sys.stdin.readline().split())
a, b = sys.stdin.readline().strip().split()

alpha = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()
alpha_score = [3, 2, 1, 2, 4, 3, 1, 3, 1, 1, 3, 1, 3, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

name_merge = ""
short_name = ""
remain_name = ""

if n < m:
    short_name = b[:n]
    remain_name = b[n:m]
else:
    short_name = a[:m]
    remain_name = a[m:n]

for i in range(min(n, m)):
    name_merge += a[i] + b[i]

name_merge = name_merge + remain_name
score_list = []

for j in range(len(name_merge)):
    score_list.append(alpha_score[alpha.index(name_merge[j])])

tmp = []

while True:
    for k in range(len(score_list) - 1):
        tmp.append((score_list[k] + score_list[k + 1]) % 10)

    score_list = tmp.copy()
    tmp.clear()

    if len(score_list) == 2:
        break

res_score = int(str(score_list[0]) + str(score_list[1]))

print("{}%".format(res_score))

# 다른 사람 풀이
# key = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# val = '32124313113132122212111221'
#
# n, m = map(int, input().split())
# a, b = input().split()
# x = ""
#
# for i in range(max(n,m)):
#     try:
#         x += a[i]
#     except :
#         pass
#     try:
#         x += b[i]
#     except:
#         pass
#
# y = x.translate(str.maketrans(key, val))
#
# while True :
#     if len(y)==2 or len(y) == 1 :
#         break
#     z = ""
#     for j in range(len(y)-1):
#         z += str((int(y[j])+int(y[j+1]))%10)
#     y = z
#
# print(f"{int(y)}%")