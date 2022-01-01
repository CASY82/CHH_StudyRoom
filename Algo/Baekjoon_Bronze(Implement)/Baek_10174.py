import sys

n = int(sys.stdin.readline())

for _ in range(n):
    word = list(sys.stdin.readline().strip().lower())
    check = True

    for i in range(len(word)//2):
        if word[i] != word[-i-1]:
            check = False
            break

    if check:
        print("Yes")
    else:
        print("No")