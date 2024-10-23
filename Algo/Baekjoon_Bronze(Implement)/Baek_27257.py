import sys

n = sys.stdin.readline().strip()

total = n.count("0")
i = len(n)-1
cnt = 0

while n[i] == "0":
    cnt += 1
    i -= 1

print(total-cnt)