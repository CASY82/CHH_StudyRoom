import sys

n = int(sys.stdin.readline())

for _ in range(n):
    zombieEat, zombieNeed = map(int, sys.stdin.readline().split())

    if zombieNeed > zombieEat:
        print("NO BRAINS")
    else:
        print("MMM BRAINS")