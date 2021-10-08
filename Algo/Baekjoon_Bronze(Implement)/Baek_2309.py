nan = []

for _ in range(9):
    nan.append(int(input()))



for i in range(len(nan)):
    for j in range(i + 1, len(nan)):
        sum_height = sum(nan)
        sum_height -= nan[i]
        sum_height -= nan[j]

        a = nan[i]
        b = nan[j]

        if sum_height == 100:
            nan.remove(a)
            nan.remove(b)
            break

    if sum_height == 100:
        break

nan.sort()

for j in nan:
    print(j)
