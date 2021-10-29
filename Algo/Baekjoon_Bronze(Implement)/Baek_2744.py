word = list(input())
new_word = []
for i in range(len(word)):
    if word[i].islower():
        new_word.append(word[i].upper())
    else:
        new_word.append(word[i].lower())

print(''.join(new_word))