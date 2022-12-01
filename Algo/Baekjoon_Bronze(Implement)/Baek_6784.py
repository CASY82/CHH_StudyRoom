import sys

n = int(sys.stdin.readline())

num_list = []
check_list = []
result = 0

for _ in range(n):
    num_list.append(sys.stdin.readline().strip())

for _ in range(n):
    check_list.append(sys.stdin.readline().strip())

for i in range(n):
    if num_list[i] == check_list[i]:
        result += 1

print(result)