import sys

re_course = sys.stdin.readline().strip()
n = int(sys.stdin.readline())
res = 0

for _ in range(n):
    course = sys.stdin.readline().strip()

    if course[:5] == re_course[:5]:
        res += 1

print(res)