# 재귀를 사용하는 방법을 좀 더 숙련시킬 필요가 있다.... 분할정복은 성공적!
n, r, c = map(int, input().split())
array = [[0 for i in range(2)] for j in range(2)]
start_num = 0
answer = 0

while n > 0:
    if n > 1:
        for i in range(2):
            for j in range(2):
                if i == 0 and j == 0:
                    array[i][j] = start_num
                elif i == 0 and j == 1:
                    array[i][j] = start_num + 2 ** (2 * (n - 1)) * 1
                elif i == 1 and j == 0:
                    array[i][j] = start_num + 2 ** (2 * (n - 1)) * 2
                elif i == 1 and j == 1:
                    array[i][j] = start_num + 2 ** (2 * (n - 1)) * 3

        if (2 ** (n - 1)) > r and (2 ** (n - 1)) > c:
            start_num = array[0][0]
        elif (2 ** (n - 1)) > r and (2 ** (n - 1)) <= c:
            start_num = array[0][1]
            c -= (2 ** (n - 1))
        elif (2 ** (n - 1)) <= r and (2 ** (n - 1)) > c:
            start_num = array[1][0]
            r -= (2 ** (n - 1))
        else:
            start_num = array[1][1]
            r -= (2 ** (n - 1))
            c -= (2 ** (n - 1))

    else:
        for i in range(2):
            for j in range(2):
                if i == 0 and j == 0:
                    array[i][j] = start_num
                elif i == 0 and j == 1:
                    array[i][j] = start_num + 1
                elif i == 1 and j == 0:
                    array[i][j] = start_num + 2
                elif i == 1 and j == 1:
                    array[i][j] = start_num + 3

        if (2 ** (n - 1)) > r and (2 ** (n - 1)) > c:
            answer = array[0][0]
        elif (2 ** (n - 1)) > r and (2 ** (n - 1)) <= c:
            answer = array[0][1]
        elif (2 ** (n - 1)) <= r and (2 ** (n - 1)) > c:
            answer = array[1][0]
        else:
            answer = array[1][1]

    n -= 1

print(answer)

#다른 사람 풀이 : 내풀이는 너무 소스가 길다...
# n,r,c = list(map(int,input().split()))
# cnt = 0
# for i in range(n-1,-1,-1):
#     tc = 0
#     if r+1 > 2**i:
#         r -= 2**i
#         tc += 2
#     if c+1 > 2**i:
#         tc += 1
#         c -= 2**i
#     cnt += (2**i)**2*tc
# print(cnt)

# def cnt(n, r, c):
#     if (n == 1):
#         if (r == 0 and c == 0):
#             return 0
#         elif (r == 0 and c == 1):
#             return 1
#         elif (r == 1 and c == 0):
#             return 2
#         else:
#             return 3
#
#     a = 2 ** (n - 1)
#     if (r < a and c < a):
#         return cnt(n - 1, r, c)
#     elif (r < a and c >= a):
#         return cnt(n - 1, r, c - a) + (a ** 2)
#     elif (r >= a and c < a):
#         return cnt(n - 1, r - a, c) + (a ** 2) * 2
#     else:
#         return cnt(n - 1, r - a, c - a) + (a ** 2) * 3
#
#
# n, r, c = map(int, input().split())
# print(cnt(n, r, c))