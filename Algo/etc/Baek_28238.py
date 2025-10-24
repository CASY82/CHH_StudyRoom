import sys

n = int(sys.stdin.readline())
schedule = []
res = 0
day_index = [1, 4]
res_days = [0, 0, 0, 0, 0]

for _ in range(n):
    schedule.append(list(map(int, sys.stdin.readline().split())))

for i in range(4):
    for j in range(i + 1, 5):
        tmp = 0
        for k in range(n):
            if schedule[k][i] == 1 and schedule[k][j] == 1:
               tmp += 1

        if res < tmp:
            res = tmp
            day_index[0] = i
            day_index[1] = j

res_days[day_index[0]] = 1
res_days[day_index[1]] = 1

print(res)
print(*res_days)