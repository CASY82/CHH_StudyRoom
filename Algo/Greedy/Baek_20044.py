import sys

team = int(sys.stdin.readline())
value = list(map(int, sys.stdin.readline().split()))

value.sort()
result = int(1e9)

for i in range(team):
    if result > (value[i] + value[len(value)-1-i]):
        result = value[i] + value[len(value)-1-i]

print(result)