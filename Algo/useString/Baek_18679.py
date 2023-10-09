import sys

n = int(sys.stdin.readline())
words = dict()

for _ in range(n):
    trans, origin = sys.stdin.readline().strip().split(" = ")

    words[trans] = origin

t = int(sys.stdin.readline())

for _ in range(t):
    words_len = int(sys.stdin.readline())
    tmp_sentence = list(sys.stdin.readline().strip().split())

    for word in tmp_sentence:
        print(words[word], end=" ")

    print()