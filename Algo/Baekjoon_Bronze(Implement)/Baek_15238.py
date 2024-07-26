import sys

n = int(sys.stdin.readline())
word = sys.stdin.readline().strip()

alpha_set = dict()

for i in range(n):
    if word[i] in alpha_set:
        alpha_set[word[i]] += 1
    else:
        alpha_set[word[i]] = 1

max_cnt = 0
max_alpha = ''

for k, v in alpha_set.items():
    if max_cnt < v:
        max_cnt = v
        max_alpha = k

print(max_alpha, max_cnt)