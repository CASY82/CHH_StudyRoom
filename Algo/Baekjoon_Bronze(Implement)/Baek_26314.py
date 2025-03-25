import sys

n = int(sys.stdin.readline())
vowels = {"a", "e", "i", "o", "u"}

for _ in range(n):
    words = sys.stdin.readline().strip()

    vo_cnt = 0
    consonant_cnt = 0

    for i in range(len(words)):
        if words[i] in vowels:
            vo_cnt += 1
        else:
            consonant_cnt += 1

    print(words)
    # 모음이 많으면 1
    if vo_cnt > consonant_cnt:
        print(1)
    else:
        print(0)