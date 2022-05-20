import sys

n = int(sys.stdin.readline())

people = list(map(int, sys.stdin.readline().split()))

origin = [i for i in range(1, n+1)]
cnt = 0

for i in range(n):
    if origin[i] != people[i]:
        cnt+=1

print(cnt)