import sys

x = int(sys.stdin.readline())
n = int(sys.stdin.readline())
result = 0

for _ in range(n):
    price, cnt = map(int, sys.stdin.readline().split())
    
    result += price * cnt

if result == x:
    print("Yes")
else:
    print("No")