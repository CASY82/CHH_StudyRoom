import sys

n = int(sys.stdin.readline())
schedule = []
res = 0
max_person_date = []

for _ in range(n):
    schedule.append(list(sys.stdin.readline().strip()))

for i in range(5):
    tmp = 0
    for j in range(n):
        if schedule[j][i] == "Y":
           tmp += 1

    if tmp == res:
        max_person_date.append(i + 1)
    elif tmp > res:
        res = tmp
        max_person_date.clear()
        max_person_date.append(i + 1)

print(",".join(map(str, max_person_date)))