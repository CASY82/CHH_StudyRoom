import sys

n = int(sys.stdin.readline())
sentence = list(sys.stdin.readline().strip().split())
res = []

for i in range(n):
    res.append(sentence[i] + "DORO")

print(" ".join(res))