import sys

while True:
    word = sys.stdin.readline().strip()

    if word == "*":
        break

    result = True

    for pair in range(1, len(word)):
        wordSet = set()
        for now in range(len(word)):
            if now + pair < len(word):
                if word[now] + word[now + pair] not in wordSet:
                    wordSet.add(word[now] + word[now + pair])
                else:
                    result = False
                    break

        if not result:
            break

    if result:
        print("{} is surprising.".format(word))
    else:
        print("{} is NOT surprising.".format(word))

# 다른 사람 풀이 참고
# def isSur(S):
#     LS = len(S)
#     for D in range(LS - 1):
#         if len(set([S[i] + S[i + D + 1] for i in range(LS - 1 - D)])) != LS - 1 - D: return True
#     return False
#
# ST = input()
#
# while ST != "*":
#     print(ST, "is", "NOT " * isSur(ST) + "surprising.")
#     ST = input()