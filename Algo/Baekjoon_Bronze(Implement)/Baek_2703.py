from string import ascii_uppercase

t = int(input())
alpha = list(ascii_uppercase)

for _ in range(t):
    word = list(input())
    crypto_rule = list(input())
    new_word = []

    for i in range(len(word)):
        if word[i] != ' ':
            new_word.append(crypto_rule[alpha.index(word[i])])
        else:
            new_word.append(' ')

    print(''.join(new_word))