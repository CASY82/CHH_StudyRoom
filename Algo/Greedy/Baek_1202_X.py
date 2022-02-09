# 답은 나오는데 당연히 시간초과
# import sys
# from collections import deque
# 
# n, k = map(int, sys.stdin.readline().split())
# jewel = []
# 
# bag = []
# 
# for _ in range(n):
#     jewel.append(list(map(int, sys.stdin.readline().split())))
# 
# for _ in range(k):
#     bag.append(int(sys.stdin.readline()))
# 
# jewel.sort(key= lambda x : (-x[1], x[0]))
# jewelDQ = deque(jewel)
# bag.sort()
# 
# # print(jewel, bag, jewelDQ)
# result = 0
# 
# for i in bag:
#     for j in range(len(jewelDQ)):
#         tmp = jewelDQ.popleft()
#         # print(tmp)
#         if tmp[0] <= i:
#             result += tmp[1]
#             break
#         else:
#             jewelDQ.append(tmp)
#     # print(jewelDQ)
# 
# print(result)

# 아... 접근 자체를 잘못하고 있던 문제... 시간초과가 나긴 했지만 그래도 로직 구현은 맞아서 다행이고
# 최소힙을 이런식으로도 활용이 가능하다는 것을 알게 되었다.
import sys
import heapq

n, k = map(int, sys.stdin.readline().split())
jewel = []
bag = []

for _ in range(n):
    heapq.heappush(jewel, list(map(int, sys.stdin.readline().split())))

for _ in range(k):
    heapq.heappush(bag, int(sys.stdin.readline()))

result = 0
tmp = []

for _ in range(k):
    weight = heapq.heappop(bag)

    while jewel and weight >= jewel[0][0]:
        [jewelWeight, jewelPrice] = heapq.heappop(jewel)
        heapq.heappush(tmp, -jewelPrice)

    if tmp:
        result -= heapq.heappop(tmp)
    elif not jewel:
        break

print(result)