import sys

candy = int(sys.stdin.readline())

cnt = 0

for t in range(1, candy - 1):
    for y in range(1, candy - 1):
        for n in range(1, candy - 1):
            if n >= y + 2 and t % 2 == 0 and t + y + n == candy:
                cnt += 1

print(cnt)