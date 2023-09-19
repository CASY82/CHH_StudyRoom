import sys

word_1 = sys.stdin.readline().strip()
word_2 = sys.stdin.readline().strip()
same = sys.stdin.readline().strip()

if same in word_1 and same in word_2:
    print("YES")
else:
    print("NO")