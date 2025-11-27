import sys

n = int(sys.stdin.readline())
sentence = sys.stdin.readline().strip().split()

res = sentence[0][0]

for i in range(1, n):
    if len(sentence[i]) < len(sentence[i - 1]):
        res += " "
    else:
        res += sentence[i][len(sentence[i - 1]) - 1]

print(res)