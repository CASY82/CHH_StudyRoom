sentence = list(input())
cipher = input()
cipher_changer = []
sentence_changer = []
result = []
count = len(cipher)

alpha = [' ', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

for i in range(len(cipher)):
    cipher_changer.append(alpha.index(cipher[i]))

for i in range(len(sentence)):
    for j in range(len(sentence[i])):
        sentence_changer.append(alpha.index(sentence[i][j]))

for i in range(len(sentence_changer)):
    if sentence_changer[i] != 0:
        tmp = sentence_changer[i] - cipher_changer[i % len(cipher_changer)]

        if tmp <= 0:
            tmp += 26

        result.append(tmp)
    else:
        result.append(0)

for i in result:
    print(alpha[i], end='')

# 좀 더 깔끔하고 간단한 다른사람의 풀이
# from string import ascii_lowercase
#
# alpha = {ascii_lowercase[i]:i+1 for i in range(26)}
# word, key, code = input(), input(), ''
#
# for i in range(len(word)):
#     W = word[i]
#     if W == ' ':
#         code += ' '
#         continue
#     K = key[i % len(key)]
#     idx = alpha[W] - alpha[K]
#     code += ascii_lowercase[idx-1]
#
# print(code)