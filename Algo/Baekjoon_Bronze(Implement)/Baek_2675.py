t = int(input())

for _ in range(t):
    counter, word = input().split()
    counter = int(counter)
    new_word = ''

    for i in range(len(word)):
        for j in range(counter):
            new_word += word[i]

    print(new_word)