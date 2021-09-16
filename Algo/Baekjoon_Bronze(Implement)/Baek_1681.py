n, l = map(int, input().split())

count = 0
num = 1

while True:
    if str(num).find(str(l)) != -1:
        num += 1
        continue

    count += 1
    if count >= n:
        break

    num += 1


print(num)

# 음.. 왜 남의 풀이를 확인하니.. 왜 난 처음에 똑같이 했는데 안됬었을까...? 그래서 find를 사용했다.
# N, L = input().split()
# count = 0
# number = 0
# while count < int(N):
#     number += 1
#     if L in str(number):
#         continue
#     count += 1
# print(number)