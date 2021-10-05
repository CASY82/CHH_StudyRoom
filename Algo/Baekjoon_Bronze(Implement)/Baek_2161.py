from collections import deque

n = int(input())
result = []
dq = deque()
dq.extend([i for i in range(1, n+1)])

while len(dq) >= 2:
    result.append(dq.popleft())
    dq.append(dq.popleft())

result.append(dq[0])

for i in result:
    print(i, end=' ')


# 다름 사람 풀이
#
# n=int(input())
# card=list()
# for i in range(1,n+1):
#     card.append(i)
# while len(card)>1:
#     print(card.pop(0),end=' ')
#     card.append(card[0])
#     card.pop(0)
# print(card[0])
