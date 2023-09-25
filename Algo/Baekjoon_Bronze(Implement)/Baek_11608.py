import sys

word = sys.stdin.readline().strip()
word_set = dict()

for i in range(len(word)):
    if word[i] not in word_set:
        word_set[word[i]] = 1
    else:
        word_set[word[i]] += 1

sorted_value = sorted(word_set.items(), key=lambda item: item[1])

if len(sorted_value) <= 2:
    print(0)
else:
    result = 0

    for k, v in sorted_value[:-2]:
        result += v

    print(result)