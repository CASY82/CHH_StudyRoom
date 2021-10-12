n = int(input())

for i in range((2 * n) - 1):
    for j in range(n):
        if i <= n - 1:
            if i >= j:
                print('*', end='')
            else:
                continue
        else:
            if ((2 * n) - 2) - i >= j:
                print('*', end='')
            else:
                continue

    print()