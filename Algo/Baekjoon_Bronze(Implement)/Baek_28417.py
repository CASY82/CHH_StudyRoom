import sys

n = int(sys.stdin.readline())

max_score = 0

for _ in range(n):
    scores = list(map(int, sys.stdin.readline().split()))

    runs = scores[:2]
    tricks = scores[2:]
    runs.sort(reverse=True)
    tricks.sort(reverse=True)

    max_score = max((runs[0] + tricks[1] + tricks[0], max_score))

print(max_score)