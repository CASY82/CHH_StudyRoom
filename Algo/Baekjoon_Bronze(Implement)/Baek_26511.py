import sys

n = int(sys.stdin.readline())

for _ in range(n):
    tmp = dict()
    res = 0
    word = sys.stdin.readline().strip()

    for i in range(len(word)):
        if word[i] not in tmp:
            tmp[word[i]] = 1
        else:
            tmp[word[i]] += 1

    sorted_dict = dict(sorted(tmp.items(), key=lambda item: item[1], reverse=True))
    setter_dict = set(sorted_dict)

    while len(setter_dict) > 2:
        item, cnt = sorted_dict.popitem()
        res += cnt
        setter_dict = set(sorted_dict)

    print(res)

# 다른 사람 풀이
# import sys
# def input():return sys.stdin.readline().rstrip()
# for _ in range(int(input())):
#     x = input()
#     lst = [0]*26
#     for i in x:
#         lst[ord(i) - ord('a')] += 1
#     while 0 in lst:
#         lst.remove(0)
#     lst.sort()
#     if len(lst) > 2:
#         print(sum(lst) - lst[-1] - lst[-2])
#     else:
#         print(0)