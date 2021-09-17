n = int(input())

for i in range(n):
    for j in range(1, n*2+1):
        if n + i >= j and n - i <= j:
            print('*', end='')
        elif n - i > j:
            print(' ', end='')

    print()