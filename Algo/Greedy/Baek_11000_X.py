import sys
import heapq

n = int(sys.stdin.readline())
class_time = []
tmp = []
cnt = 1

for _ in range(n):
    class_time.append(list(map(int, sys.stdin.readline().split())))

class_time.sort(key=lambda x:x[0])
heapq.heappush(tmp, class_time[0][1])

#우선순위 큐를 활용하는 방법을 생각하자(정렬)

# for i in range(1, len(class_time)):
#     while tmp:
#         num, classroom = heapq.heappop(tmp)
#         num *= -1
#
#         if classroom[0] < class_time[i][0] < classroom[1]:
#             heapq.heappush(tmp, (-num, classroom))
#             heapq.heappush(tmp, (-(num+1), class_time[i]))
#             cnt += 1
#             break
#         elif classroom[0] < class_time[i][0] and classroom[1] < class_time[i][1]:
#             heapq.heappush(tmp, (-(num+1), class_time[i]))
#             break


for i in range(1, n):
    #이전에 풀때 이거랑 비슷한 문제가 있었는데... 그 해법에 우선순위 큐를 더한 문제였다... 왜자꾸 틀리냐...
    if tmp[0] > class_time[i][0]:
        heapq.heappush(tmp, class_time[i][1])
    else:
        heapq.heappop(tmp)
        heapq.heappush(tmp, class_time[i][1])

print(len(tmp))