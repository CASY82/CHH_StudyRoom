import sys

alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
cnt = 1

while True:
    word = sys.stdin.readline().strip()
    dif = sys.stdin.readline().strip()
    result = True

    if word == "END" and dif == "END":
        break

    word_cnt = [0 for i in range(26)]
    dif_cnt = [0 for i in range(26)]

    if len(word) != len(dif):
        result = False
    else:
        for i in range(len(word)):
            word_cnt[alpha.index(word[i])] += 1
            dif_cnt[alpha.index(dif[i])] += 1

        for i in range(26):
            if word_cnt[i] != dif_cnt[i]:
                result = False
                break

    print("Case {}: ".format(cnt), end="")
    if result:
        print("same")
    else:
        print("different")

    cnt += 1