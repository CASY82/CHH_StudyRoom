import sys

n = int(sys.stdin.readline())
res = []

for _ in range(n):
    x_index, word = sys.stdin.readline().strip().split()

    for i in range(len(x_index)):
        if x_index[i].upper() == "X":
            res.append(word[i].upper())

print("".join(res))