import sys

n = int(sys.stdin.readline())
chang = 100
sang = 100

for _ in range(n):
    c_score, s_score = map(int, sys.stdin.readline().split())

    if s_score > c_score:
        chang -= s_score
    elif s_score < c_score:
        sang -= c_score
    else:
        continue

print(chang)
print(sang)