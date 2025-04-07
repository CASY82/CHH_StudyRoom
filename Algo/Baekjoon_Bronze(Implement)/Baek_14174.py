import sys

n = int(sys.stdin.readline())

alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
cnt = [0 for _ in range(26)]

for _ in range(n):
    word1, word2 = sys.stdin.readline().strip().split()
    tmp1 = [0 for _ in range(26)]
    tmp2 = [0 for _ in range(26)]

    for i in range(len(word1)):
        tmp1[alpha.index(word1[i])] += 1

    for j in range(len(word2)):
        tmp2[alpha.index(word2[j])] += 1

    for index in range(26):
        cnt[index] += max(tmp1[index], tmp2[index])

for k in range(26):
    print(cnt[k])