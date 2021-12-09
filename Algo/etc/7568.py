import sys

n = int(sys.stdin.readline())
people = []
rank = [1 for i in range(n)]

for _ in range(n):
    people.append(list(map(int, sys.stdin.readline().split())))

for i in range(n):
    for j in range(i+1, n):
        if people[i][0] < people[j][0] and people[i][1] < people[j][1]:
            rank[i] += 1
        elif people[i][0] > people[j][0] and people[i][1] > people[j][1]:
            rank[j] += 1

for i in rank:
    print(i, end=' ')