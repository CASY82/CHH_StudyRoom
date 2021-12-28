import sys

w = []
k = []

for _ in range(10):
    score = int(sys.stdin.readline())

    w.append(score)

for _ in range(10):
    score = int(sys.stdin.readline())

    k.append(score)

w.sort(reverse = True)
k.sort(reverse = True)

print(sum(w[0:3]), sum(k[0:3]))