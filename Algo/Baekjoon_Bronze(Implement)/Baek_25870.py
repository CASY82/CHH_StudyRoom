import sys

sentence = sys.stdin.readline().strip()

alpha = []
alpha_cnt = []

for i in range(len(sentence)):
    if sentence[i] not in alpha:
        alpha.append(sentence[i])
        alpha_cnt.append(1)
    else:
        alpha_cnt[alpha.index(sentence[i])] += 1

even_cnt = 0
odd_cnt = 0

for j in alpha_cnt:
    if j % 2 == 0:
        even_cnt += 1
    else:
        odd_cnt += 1

if odd_cnt == 0:
    print(0)
elif even_cnt == 0:
    print(1)
else:
    print(2)