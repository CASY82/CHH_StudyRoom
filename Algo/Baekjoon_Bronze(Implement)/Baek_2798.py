n, m = map(int, input().split())

card = list(map(int, input().split()))
result = []

for i in range(len(card)):
    for j in range(i+1, len(card)):
        for k in range(j+1, len(card)):
            result.append(card[i] + card[j] + card[k])

check = 999999
num = 0

for i in result:
    if i <= m:
        if i == m:
            num = i
            break
        else:
            if abs(i - m) < check:
                check = abs(i - m)
                num = i

print(num)

#반례
# 5 11
# 1 2 5 6 16

#짧은 코드 첨부 itertools를 이용한 방법 이게 가장 좋아보인다.
# import itertools
#
# n, m = map(int, input().split())
# nums = map(int, input().split())
# print(max([sum(x) for x in itertools.combinations(nums, 3) if sum(x) <= m]))