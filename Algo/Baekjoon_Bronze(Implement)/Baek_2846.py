import sys

n = int(sys.stdin.readline())
pi = list(map(int, sys.stdin.readline().split()))
result = 0
tmp = 0
num_list = []

for i in pi:
    if tmp < i:
        tmp = i
        num_list.append(i)
    else:
        tmp = i
        if result < abs(num_list[0] - num_list[-1]):
            result = abs(num_list[0] - num_list[-1])

        num_list.clear()
        num_list.append(i)

if result < abs(num_list[0] - num_list[-1]):
    result = abs(num_list[0] - num_list[-1])

print(result)