'''
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *
'''

n = int(input())

for i in range(1, n*2):
    for j in range(1, n*2 + 1):
        if n - abs(n - i) >= j or (n + 1) + abs(n - i) <= j:
            print('*', end='')
        else:
            print(' ', end='')

    print()