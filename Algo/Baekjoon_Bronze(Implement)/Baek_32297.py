import sys

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

index = 0
check = ["g", "o", "r", "i"]

for i in range(len(s)):
    if index == 4:
        break

    if check[index] == s[i]:
        index += 1
    else:
        index = 0

if index == 4:
    print("YES")
else:
    print("NO")