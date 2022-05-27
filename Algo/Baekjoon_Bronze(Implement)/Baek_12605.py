import sys

t = int(sys.stdin.readline())

for i in range(t):
    word_arr = sys.stdin.readline().strip().split()

    word_arr.reverse()

    print("Case #{}:".format(i+1), *word_arr)