import sys

check = ["u", "o", "s", "p", "c"]

n = int(sys.stdin.readline())
words = sys.stdin.readline().strip()
res = 99999999999999999

for c in check:
    res = min(words.count(c), res)

print(res)