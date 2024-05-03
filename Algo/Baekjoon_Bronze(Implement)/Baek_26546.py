import sys

n = int(sys.stdin.readline())

for _ in range(n):
    word, fir, sec = sys.stdin.readline().strip().split()

    print(word[:int(fir)] + word[int(sec):])