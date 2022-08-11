import sys

t = int(sys.stdin.readline())

for _ in range(t):
    word1, word2 = sys.stdin.readline().strip().split()

    word1_list = list(word1)
    word2_list = list(word2)

    word1_list.sort()
    word2_list.sort()
    result = True

    if len(word1_list) != len(word2_list):
        result = False
    else:
        for i in range(len(word1_list)):
            if word1_list[i] != word2_list[i]:
                result = False
                break

    if result:
        print("{0} & {1} are anagrams.".format(word1, word2))
    else:
        print("{0} & {1} are NOT anagrams.".format(word1, word2))