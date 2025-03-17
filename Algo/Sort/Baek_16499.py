import sys

n = int(sys.stdin.readline())

tmp = dict()

for _ in range(n):
    word = list(sys.stdin.readline().strip())

    word.sort()
    tmp_word = "".join(word)
    # print(tmp_word)

    if tmp_word not in tmp:
        tmp[tmp_word] = 1
    else:
        tmp[tmp_word] += 1

# count = sum(1 for value in tmp.values() if value >= 1)

# print(count)
print(len(tmp))