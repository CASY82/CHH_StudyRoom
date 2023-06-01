import sys

first = list(map(int, sys.stdin.readline().split()))
second = list(map(int, sys.stdin.readline().split()))

result = True

for i in range(5):
    if first[i] == second[i]:
        result = False
        break

if result:
    print("Y")
else:
    print("N")