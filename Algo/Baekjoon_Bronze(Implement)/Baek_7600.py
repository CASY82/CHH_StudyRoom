import sys

while True:
    sentence = sys.stdin.readline().strip()

    if sentence == "#":
        break

    alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
    alpha_cnt = [0 for _ in range(26)]

    sentence = sentence.lower()

    for i in range(len(sentence)):
        if sentence[i] in alpha:
            alpha_cnt[alpha.index(sentence[i])] += 1

    print(26 - alpha_cnt.count(0))