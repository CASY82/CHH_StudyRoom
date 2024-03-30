import sys

word = sys.stdin.readline().strip()
a_cnt = 0
b_cnt = 0

for i in range(len(word)):
    if word[i] == "A":
        a_cnt += 1
    else:
        b_cnt += 1

print("{0} : {1}".format(a_cnt, b_cnt))