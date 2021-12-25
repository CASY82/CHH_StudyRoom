import sys

word = sys.stdin.readline().strip()
check = True


for i in range(len(word)//2):
    if word[i] != word[len(word) - 1 - i]:
        check = False
        break

if check:
    print(1)
else:
    print(0)