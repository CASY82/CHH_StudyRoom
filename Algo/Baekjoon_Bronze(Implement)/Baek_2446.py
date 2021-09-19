n = int(input())

for i in range(n*2-1):
    for j in range(1, n*2):
        if i < n :
            if i < j and (n*2 - 1) - i >= j:
                print('*', end='')
            elif (n*2 - 1) - i < j:
                continue
            else:
                print(' ', end='')
        else:
            if (n*2-2 - i) < j and (n*2 - 1) - (n*2-2 - i) >= j:
                print('*', end='')
            elif (n * 2 - 1) - (n*2-2 - i) < j:
                continue
            else:
                print(' ', end='')
    print()



# 간단한 풀이
# n = int(input())
# for i in range(n, 0, -1):
#     a = '*' * (2 * i - 1)
#     b = ' ' * (n-i)
#     print(b + a)
# for i in range(1, n):
#     a = '*' * (2 * i + 1)
#     b = ' ' * (n-1-i)
#     print(b + a)