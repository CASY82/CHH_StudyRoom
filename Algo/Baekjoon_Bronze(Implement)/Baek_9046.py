import sys

t = int(sys.stdin.readline())

alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split()
cnt = [0 for _ in range(26)]

for _ in range(t):
    sentense = sys.stdin.readline().strip()
    result = []

    for i in range(len(alpha)):
        cnt[i] = sentense.count(alpha[i])

    for j in range(26):
        if cnt[j] == max(cnt):
            result.append(alpha[j])

    if len(result) >= 2:
        print("?")
    else:
        print(result[0])