import sys

word_in = sys.stdin.readline().strip()

replace_dict = {
    "a": "4",
    "e": "3",
    "i": "1",
    "o": "0",
    "s": "5"
}

print("".join([replace_dict[word] if word in replace_dict else word for word in list(word_in)]))

# 시간 초과
# result = ""

# 문자열 덧셈은 시간 복잡도가 증가함
# for i in range(len(word)):
#     if word[i] in replace_dict:
#         result += replace_dict[word[i]]
#     else:
#         result += word[i]

