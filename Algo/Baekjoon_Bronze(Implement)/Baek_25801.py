import sys

alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
alpha_cnt = [0 for i in range(26)]

word = sys.stdin.readline().strip()

for i in range(len(word)):
    alpha_cnt[alpha.index(word[i])] += 1

odd = 0
even = 0

for num in alpha_cnt:
    if num == 0:
        continue

    if num % 2 == 0:
        even += 1
    else:
        odd += 1

if odd == 0:
    print(0)
elif even == 0:
    print(1)
else:
    print("0/1")