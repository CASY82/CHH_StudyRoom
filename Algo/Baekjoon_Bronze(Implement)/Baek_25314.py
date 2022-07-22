import sys

n = int(sys.stdin.readline())

cnt = n // 4

for _ in range(cnt):
    print("long", end=" ")
print("int")