import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque()
res_min_stu_num = float('inf') # 제일 작은 학생 넘버
res_max_stu = 0 # 최대 학생수

for _ in range(n):
    command = list(sys.stdin.readline().strip().split())

    if command[0] == "1":
        queue.append(int(command[1]))
        if res_max_stu < len(queue):
            res_max_stu = max(res_max_stu, len(queue))
            res_min_stu_num = queue[-1]
        elif res_max_stu == len(queue):
            res_min_stu_num = min(res_min_stu_num, queue[-1])
    else:
        if queue:
            queue.popleft()

print(res_max_stu, res_min_stu_num)