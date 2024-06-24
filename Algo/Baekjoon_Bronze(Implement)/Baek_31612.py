import sys

n = int(sys.stdin.readline())
word = sys.stdin.readline().strip()
res = 0

for i in range(n):
    if word[i] == "j":
        res += 2
    elif word[i] == "i":
        res += 2
    elif word[i] == "o":
        res += 1

print(res)