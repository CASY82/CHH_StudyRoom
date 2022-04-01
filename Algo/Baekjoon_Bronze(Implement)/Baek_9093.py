import sys

n = int(sys.stdin.readline())

for _ in range(n):
    sentence = list(sys.stdin.readline().strip().split())

    for i in range(len(sentence)):
        sentence[i] = sentence[i][::-1]

    print(' '.join(sentence))