n = int(input())

for i in range(n-1, -1, -1):
    for j in range(1, n*2):
        if n + i >= j and n - i <= j:
            print('*', end='')
        elif n - i > j:
            print(' ', end='')

    print()
