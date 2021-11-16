n = int(input())
count = 0

for _ in range(n):
    word = input()
    word_list = []
    check = word[0]
    fin = True

    word_list.append(word[0])
    for i in range(len(word)):
        if word[i] != check:
            if word[i] in word_list:
                fin = False
                break
            word_list.append(word[i])

        check = word[i]

    if fin:
        count += 1

print(count)