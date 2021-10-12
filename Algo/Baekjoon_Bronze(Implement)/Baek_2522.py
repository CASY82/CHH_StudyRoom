n = int(input())

for i in range((2 * n) - 1):
    for j in range(n):
        if j >= abs(n - 1 - i):
            print('*', end ='')
        else:
            print(' ', end ='')

    print()