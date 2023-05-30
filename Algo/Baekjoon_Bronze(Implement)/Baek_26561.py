import sys

t = int(sys.stdin.readline())

for _ in range(t):
    person, time = map(int, sys.stdin.readline().split())

    dead = time // 7
    born = time // 4

    print(person + born - dead)