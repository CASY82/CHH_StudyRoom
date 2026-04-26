# Fabryka butów
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, k = map(int, sys.stdin.readline().split())
    people = list(map(int, sys.stdin.readline().split()))

    last = sum(people)
    tmp = [last]

    for i in range(n - 1):
        last -= people[i]
        tmp.append(last)

    tmp2 = []

    for j in range(1, n + 1):
        tmp2.append(tmp[j - 1] * j - tmp[j - 1] * k)

    print(max(tmp2))