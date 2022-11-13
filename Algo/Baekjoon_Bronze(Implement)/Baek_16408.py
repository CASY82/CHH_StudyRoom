import sys

card = list(sys.stdin.readline().strip().split())
rank = dict()

for i in range(len(card)):
    if card[i][0] not in rank:
        rank[card[i][0]] = 1
    else:
        rank[card[i][0]] += 1

print(rank[max(rank,key=rank.get)])