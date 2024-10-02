import sys

n = int(sys.stdin.readline())
dolls = list(map(int, sys.stdin.readline().split()))

dolls.sort()
now = [dolls[0]]

for i in range(1, n):
    check = True
    for j in range(len(now)):
        if dolls[i] > now[j]:
            now[j] = dolls[i]
            check = False
            break

    if check:
        now.append(dolls[i])

print(len(now))

# 다른 사람 풀이
# a = int(input())
# b = list(map(int, input().split()))
# k = list(set(b))
# lst = [b.count(i)for i in k]
# print(max(lst))