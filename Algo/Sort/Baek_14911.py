import sys

num_list = list(map(int, sys.stdin.readline().split()))
sum_checker = int(sys.stdin.readline())

result = set()

length = len(num_list)

for i in range(length):
    for j in range(i + 1, length):
        if num_list[i] + num_list[j] == sum_checker:
            result.add((min(num_list[i], num_list[j]), max(num_list[i], num_list[j])))

result_list = list(result)
result_list.sort(key=lambda x: (x[0], x[1]))

for cnt in range(len(result_list)):
    print(result_list[cnt][0], result_list[cnt][1])

print(len(result_list))