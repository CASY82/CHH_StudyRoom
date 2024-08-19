import sys

n = int(sys.stdin.readline())

word1 = sys.stdin.readline().strip()
word2 = sys.stdin.readline().strip()
res = 0

for i in range(n):
    tmp = abs(ord(word1[i]) - ord(word2[i]))
    res += min(tmp, 26 - tmp)

print(res)