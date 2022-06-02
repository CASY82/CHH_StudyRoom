import sys

word = list(sys.stdin.readline().strip())
word.reverse()
print("".join(word))