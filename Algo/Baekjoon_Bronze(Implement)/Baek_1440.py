time = list(map(int, input().split(':')))
count = 0

for i in range(len(time)):
    if time[i] >= 60 or sum(time) == 0 or min(time) > 12:
        count = 0
        break

    if time[i] <= 12 and time[i] >= 1:
        count += 2

print(count)