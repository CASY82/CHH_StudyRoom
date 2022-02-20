import sys
sys.setrecursionlimit(10 ** 6)

n = int(sys.stdin.readline())
color_cost = []

for _ in range(n):
    color_cost.append(list(map(int, sys.stdin.readline().split())))

house = [[0 for _ in range(3)] for _ in range(len(color_cost))]

def dp(x, color_cost, house):
    if x >= len(color_cost):
        return

    if x == 0:
        for i in range(3):
            house[x][i] = color_cost[x][i]

    else:
        for i in range(3):
            if i == 0:
                house[x][i] = min(house[x - 1][1] + color_cost[x][i], house[x - 1][2] + color_cost[x][i])
            elif i == 1:
                house[x][i] = min(house[x - 1][0] + color_cost[x][i], house[x - 1][2] + color_cost[x][i])
            else:
                house[x][i] = min(house[x - 1][0] + color_cost[x][i], house[x - 1][1] + color_cost[x][i])

    dp(x+1, color_cost, house)

dp(0, color_cost, house)

print(min(house[-1]))

# 다른 사람 풀이

# import sys
# N=int(sys.stdin.readline())
#
# lst=[]
# for i in range(N) :
#     lst.append(list(map(int,sys.stdin.readline().split())))
#
# for i in range(1,N) :
#     lst[i][0]=lst[i][0]+min(lst[i-1][1],lst[i-1][2])
#     lst[i][1]=lst[i][1]+min(lst[i-1][0],lst[i-1][2])
#     lst[i][2]=lst[i][2]+min(lst[i-1][0],lst[i-1][1])
#
# print( min(lst[N-1][0],lst[N-1][1],lst[N-1][2])  )