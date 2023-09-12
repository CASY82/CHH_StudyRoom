import sys

word = sys.stdin.readline().strip()

check = "M O B I S".split(" ")
table = [0 for _ in range(5)]

for w in word:
    if w in check:
        table[check.index(w)] = 1

if sum(table) == 5:
    print("YES")
else:
    print("NO")