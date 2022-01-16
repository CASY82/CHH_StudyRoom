# 시간 초과
# import sys
# from collections import deque
# 
# t = int(sys.stdin.readline())
# 
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     stock = list(map(int, sys.stdin.readline().split()))
#     temp = deque(stock)
#     benefit = 0
# 
#     i = 0
#     while temp:
#         if max(temp) > temp[i]:
#             benefit += max(temp) - temp[i]
# 
#         temp.popleft()
# 
#     print(benefit)

# 여전히 시간초과 사실 크게 달라진건 없어서 시간 초과 같긴했다. pypy로도 통과 실패
# import sys
# from collections import deque
# 
# t = int(sys.stdin.readline())
# 
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     stock = deque(list(map(int, sys.stdin.readline().split())))
#     benefit = 0
# 
#     for _ in range(len(stock)):
#         if max(stock) > stock[0]:
#             benefit += max(stock) - stock[0]
# 
#         stock.popleft()
# 
#     print(benefit)

# 91%에서 시간초과;;;;
# import sys
#
# t = int(sys.stdin.readline())
#
# for _ in range(t):
#     n = int(sys.stdin.readline())
#     stock = list(map(int, sys.stdin.readline().split()))
#     benefit = 0
#
#     while len(stock) > 0:
#         temp = stock[:stock.index(max(stock))]
#         benefit += (max(stock) * len(temp)) - sum(temp)
#         stock = stock[stock.index(max(stock))+1:]
#
#     print(benefit)

# 계속 시간초과나서 결국 보고함. 막상 보고나니 어이가 없다...
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    stock = list(map(int, sys.stdin.readline().split()))
    benefit=0
    max=0
    for i in range(len(stock) - 1, -1, -1):
        if(stock[i] > max):
            max = stock[i]
        else:
            benefit+= max - stock[i]
    print(benefit)