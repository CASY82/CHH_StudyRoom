import string

word = input()
word = word.upper()
word_list = [i for i in string.ascii_uppercase]
word_count_list = [0 for _ in range(len(word_list))]
result = ''
count = 0

for i in range(len(word_list)):
    word_count_list[word_list.index(word_list[i])] += word.count(word_list[i])

for i in range(len(word_list)):
    if word_count_list[i] == max(word_count_list):
        count += 1

if count > 1:
    result = '?'
else:
    result = word_list[word_count_list.index(max(word_count_list))]

print(result)

#참고

# words = input().upper()
# unique_words = list(set(words))  # 입력받은 문자열에서 중복값을 제거
#
# cnt_list = []
# for x in unique_words :
#     cnt = words.count(x)
#     cnt_list.append(cnt)  # count 숫자를 리스트에 append
#
# if cnt_list.count(max(cnt_list)) > 1 :  # count 숫자 최대값이 중복되면
#     print('?')
# else :
#     max_index = cnt_list.index(max(cnt_list))  # count 숫자 최대값 인덱스(위치)
#     print(unique_words[max_index])