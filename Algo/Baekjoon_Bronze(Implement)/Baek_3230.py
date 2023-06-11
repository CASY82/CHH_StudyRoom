import sys

n, m = map(int, sys.stdin.readline().split())

first = []
second = []

for i in range(n):
    ranking = int(sys.stdin.readline())-1

    first.insert(ranking, i+1)

tmp = first[:m]
tmp.reverse()

for j in tmp:
    ranking = int(sys.stdin.readline())-1

    second.insert(ranking, j)

for result in range(3):
    print(second[result])