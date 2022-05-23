import sys

word = sys.stdin.readline().strip()

result = set()

for i in range(1, len(word)):
    length = i

    checker = [word[i:i+length] for i in range(0, len(word))]

    for j in checker:
        result.add(j)

print(len(result)+1)

#다른 사람 풀이
#
# s = input()
# partial_str = set()
# for k in range(len(s)):
#     for j in range(k+1):
#         partial_str.add(s[j:j+len(s)-1-k+1])
# print(len(list(partial_str)))