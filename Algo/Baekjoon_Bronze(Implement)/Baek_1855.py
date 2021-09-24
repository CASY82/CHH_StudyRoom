k = int(input())
word = input()
z = len(word)//k
crypto_word = [['x' for i in range(k)] for j in range(z)]
word_count = 0

for i in range(z):
    for j in range(k):
        if i % 2 == 0:
            crypto_word[i][j] = word[word_count]
        else:
            crypto_word[i][(k-1) - j] = word[word_count]

        word_count += 1

for i in range(k):
    for j in range(z):
        print(crypto_word[j][i], end='')

'''
4
aeimnjfbcgkoplhd
abcdefghijklmnop

3
aeimnjfbcgkoplh
ajfopenbklimcgh
'''