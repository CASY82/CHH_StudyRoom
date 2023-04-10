import sys

mbti = sys.stdin.readline().strip()
result = []
mbti_list = [['E', 'I'], ['S', 'N'], ['T', 'F'], ['J', 'P']]

for word in range(len(mbti)):
    if mbti[word] == mbti_list[word][0]:
        result.append(mbti_list[word][1])
    else:
        result.append(mbti_list[word][0])

print("".join(result))