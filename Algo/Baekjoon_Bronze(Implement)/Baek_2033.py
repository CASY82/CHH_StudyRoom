n = list(map(int, input()))

if len(n) > 1:
    for i in range(len(n)-1, 0, -1):
        if n[i] >= 5:
            n[i-1] += 1

        n[i] = 0

    for i in n:
        print(i, end='')

else:
    print(n[0])
