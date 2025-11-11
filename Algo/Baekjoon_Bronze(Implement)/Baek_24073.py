import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

check = ["I", "O", "I"]
index = 0
res = False

for i in range(n):
    if index > 2:
        res = True
        break

    if check[index] == s[i]:
        index += 1

if index > 2:
    res = True

if res:
    print("Yes")
else:
    print("No")