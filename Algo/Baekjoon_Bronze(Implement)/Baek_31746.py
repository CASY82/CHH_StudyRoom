import sys

n = int(sys.stdin.readline())

word = "SciComLove"
re_word = word[::-1]

if n % 2 == 0:
    print(word)
else:
    print(re_word)