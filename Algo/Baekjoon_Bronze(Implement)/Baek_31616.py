import sys

n = int(sys.stdin.readline())
word = list(sys.stdin.readline().strip())

check = set(word)

if len(check) == 1:
    print("Yes")
else:
    print("No")