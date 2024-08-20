import sys

t = int(sys.stdin.readline())

for _ in range(t):
    index = 1
    res = 0
    tmp = []

    while True:
        l = int(sys.stdin.readline())

        if l == 0:
            break

        tmp.append(l)

    tmp.sort(reverse=True)

    for land in tmp:
        res += 2 * (land ** index)
        index += 1

    if res > 5000000:
        print("Too expensive")
    else:
        print(res)

# 다른 사람 풀이

# for _ in range(int(input())):
#     L = []
#     a=5*(10**6)
#     while True:
#         n = int(input())
#         if n == 0:
#             break
#         L.append(n)
#     L.sort(reverse=True)
#     for i in range(len(L)):
#         L[i] = 2*(L[i]**(i+1))
#     if sum(L) > a:
#         print("Too expensive")
#     else:
#         print(sum(L))
