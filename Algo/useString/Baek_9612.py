import sys

words_dict = dict()

n = int(sys.stdin.readline())

for _ in range(n):
    word = sys.stdin.readline().strip()

    if word not in words_dict:
        words_dict[word] = 1
    else:
        words_dict[word] += 1

max_value = max(words_dict.values())
max_val = []

for key, value in words_dict.items():
    if value == max_value:
        max_val.append([key, value])

max_val.sort(key=lambda x: x[0])

print(*max_val[-1])