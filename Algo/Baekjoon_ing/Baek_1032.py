#드디어 거의 혼자 풀 수 있게 되었는가 한번에 맞추었다!
N = int(input())
word_list = []

for i in range(N):
    words = input()
    word_list.append(words)

result_word = list(word_list[0])

for i in range(1, len(word_list)):
    compare_word = list(word_list[i])

    for j in range(len(result_word)):
        if result_word[j] == compare_word[j]:
            continue
        else:
            result_word[j] = "?"


print("".join(result_word))
