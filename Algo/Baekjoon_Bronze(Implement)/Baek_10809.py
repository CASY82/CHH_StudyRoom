word = input()
alpha = [-1] * 26

for i in range(len(word)):
    if alpha[ord(word[i]) - 97] == -1:
        alpha[ord(word[i]) - 97] = i
    else:
        continue

for i in alpha:
    print(i, end=' ')