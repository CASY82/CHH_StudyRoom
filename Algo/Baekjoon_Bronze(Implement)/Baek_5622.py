word = input()

timer = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10]
word_list = ['', '', 'ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
result = 0

for i in range(len(word)):
    for j in range(len(word_list)):
        if word[i] in word_list[j]:
            result += timer[j]

print(result)