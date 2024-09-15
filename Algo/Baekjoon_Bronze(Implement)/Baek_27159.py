import sys

n = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split()))

now = card[0]
card_set = []
tmp = [now]
res = 0

for i in range(1, n):
    if card[i] - now == 1:
        tmp.append(card[i])
        now = card[i]
    else:
        card_set.append(tmp)
        now = card[i]
        tmp = [now]

card_set.append(tmp)

for i in card_set:
    res += i[0]

print(res)

# 다른 사람 풀이
# p=0
# print(sum(i*(p-(p:=i)<-1) for i in map(int,[*open(0)][1].split())))