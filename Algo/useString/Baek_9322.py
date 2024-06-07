import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    pKey1 = list(sys.stdin.readline().strip().split())
    pKey2 = list(sys.stdin.readline().strip().split())
    crypt_sentence = list(sys.stdin.readline().strip().split())

    tmp = []
    result = []
    for i in range(n):
        tmp.append((pKey2[i], crypt_sentence[i]))

    for j in range(n):
        for k in range(n):
            if pKey1[j] == tmp[k][0]:
                result.append(tmp[k][1])
                continue

    print(" ".join(result))

# 다른 사람 풀이

# a = int(input())
#
# for _ in range(a):
#     length = int(input())
#     l1 = input().split()
#     l2 = input().split()
#
#     indexList = []
#     for item in l1:
#         indexList.append(l2.index(item))
#
#     secret = input().split()
#
#     resultList = []
#
#     for index in indexList:
#         resultList.append(secret[index])
#     print(*resultList)