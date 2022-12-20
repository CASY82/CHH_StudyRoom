import sys

t = int(sys.stdin.readline())

for i in range(t):
    n = int(sys.stdin.readline())

    word = list(sys.stdin.readline().strip().split())

    print("Case {0}: This list contains {1} sheep.".format(i+1, word.count("sheep")))
    print()