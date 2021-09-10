n = int(input())
count = 1
time = 0

while n > 0:
    n -= count

    if count < n:
        count += 1
    else:
        count = 1

    time += 1

print(time)