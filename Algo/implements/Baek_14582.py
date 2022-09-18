import sys

zeminis = list(map(int, sys.stdin.readline().split()))
startlinks = list(map(int, sys.stdin.readline().split()))
reversal = []
zeminis_result = 0
startlinks_result = 0

for times in range(9):
    zeminis_result += zeminis[times]
    # 이기고 있어야 함
    if zeminis_result > startlinks_result:
        startlinks_result += startlinks[times]
        reversal.append(0)
    # 비기거나 지고 있다.
    else:
        #그러므로 1추가
        startlinks_result += startlinks[times]
        reversal.append(1)

if reversal.count(0) > 0:
    print("Yes")
else:
    print("No")