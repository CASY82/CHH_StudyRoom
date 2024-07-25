import sys

sentence = list(sys.stdin.readline().strip())
n = int(sys.stdin.readline())

for _ in range(n):
    i, j = map(int, sys.stdin.readline().split())

    sentence[i], sentence[j] = sentence[j], sentence[i]

print("".join(sentence))