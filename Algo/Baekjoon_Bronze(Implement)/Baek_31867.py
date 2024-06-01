import sys

n = int(sys.stdin.readline())
k = sys.stdin.readline().strip()

odd = 0
even = 0

for i in range(len(k)):
    if int(k[i]) % 2 == 0:
        even += 1
    else:
        odd += 1

if odd > even:
    print(1)
elif odd < even:
    print(0)
else:
    print(-1)
