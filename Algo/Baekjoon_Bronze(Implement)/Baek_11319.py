vowel = ['A','E','I','O','U','a','e','i','o','u']

S = int(input())

for _ in range(S):
    sentense = input().split()
    sentense = ''.join(sentense)
    vowelCnt = 0

    for word in vowel:
        if word in sentense:
            vowelCnt += sentense.count(word)

    print(len(sentense)-vowelCnt, vowelCnt)