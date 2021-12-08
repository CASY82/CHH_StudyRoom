#수행시간이 너무 길다... 아직 재귀를 정말 못하는듯
import sys

n = int(sys.stdin.readline())

arr = [[0 for i in range(4*(n-1)+1)] for j in range(4*(n-1)+1)]

def recurs(n, k, first):
    if n <= 1:
        arr[(4*(first-1)+1) // 2][(4*(first-1)+1) // 2] = '*'
        return

    for i in range(k*2, 4*(n-1)+1+(k*2)):
        for j in range(k*2, 4*(n-1)+1+(k*2)):
            if i == k*2 or i == 4*(n-1)+(k*2):
                arr[i][j] = '*'
            else:
                if j == k*2 or j == 4*(n-1)+(k*2):
                    arr[i][j] = '*'
                else:
                    arr[i][j] = ' '

    recurs(n - 1, k + 1, first)

recurs(n, 0, n)

for i in range(len(arr)):
    for j in range(len(arr)):
        print(arr[i][j], sep='', end='')

    print()

# 처음 세운 코드 이걸 기반으로 배열을 추후 생각해내었다.
# def recurs(n):
#     if n < 1:
#         print('*')
#         return 0
#
#     for i in range(4*(n-1)+1):
#         for j in range(4*(n-1)+1):
#             if i == 0 or i == 4*(n-1):
#                 print('*', end='')
#             else:
#                 if j == 0 or j == 4*(n-1):
#                     print('*', end='')
#                 else:
#                     print(' ', end='')
#         print()

#실행속도도 빠르고 굉장히 잘 정리된 코드 발견...
# n = int(input())
#
# a = ['*']
#
# for i in range(1,n):
#     x = [a[0]+'****']
#     x.append('*'+' '*(len(x[0])-2)+'*')
#
#     for i in range(len(a)):
#         a[i] = '* '+a[i]+' *'
#
#     a = x+a+x[::-1]
#
#
# print('\n'.join(a))