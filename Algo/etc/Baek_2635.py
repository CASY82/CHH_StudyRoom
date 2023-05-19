import sys

first = int(sys.stdin.readline())
result = 0
result_arr = []

for i in range(first, -1, -1):
    tmp = i
    num_list = [first]
    while tmp >= 0:
        num_list.append(tmp)
        tmp = num_list[-2] - tmp

    if len(num_list) > result:
        result_arr = num_list.copy()
        result = len(num_list)

print(result)
print(*result_arr)