import sys

n = int(sys.stdin.readline())
res = False

for _ in range(n):
    word = sys.stdin.readline().strip()

    if 'anj' == word:
        res = True

if res:
    print("뭐야;")
else:
    print("뭐야?")