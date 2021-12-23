import sys
from collections import Counter

word = sys.stdin.readline().strip()
count = Counter(word)
check = True
cnt = 0

for i in count.values():
    if i % 2 == 1:
        cnt += 1

if cnt > 1:
    check = False

if check:
    result = ['0' for i in range(len(word))]
    i = 0
    word = list(word)
    word.sort(reverse=True)

    while word:
        if len(word) > 1 and word[-1] == word[-2]:
            result[i] = word.pop()
            result[len(result)-1-i] = word.pop()
            i += 1
        else:
            result[len(result) // 2] = word.pop()

    print(''.join(result))
else:
    print("I'm Sorry Hansoo")

#다른 사람 풀이
# data = input()
# data_chr = set(data)
# num_chr = {s: data.count(s) for s in data_chr}
# odd_chr = {s: c for s, c in num_chr.items() if c % 2 != 0}
#
# if len(odd_chr) > 1:
#     print("I'm Sorry Hansoo")
# else:
#     if odd_chr:
#         mid = list(odd_chr)[0]
#         num_chr[mid] -= 1
#     else:
#         mid = ""
#
#     base = ""
#     chrs = sorted(list(data_chr))
#     for c in chrs:
#         base += c * int(num_chr[c]/2)
#
#     print(base + mid + base[::-1])

# 다른 사람 풀이 2
# S = input()
# lst = [0] * 26
# for s in S:
#     lst[ord(s)-65] += 1
# check = 0
# tmp = ''
# ans = ''
# for x in range(len(lst)):
#     if lst[x] % 2 == 1:
#         check += 1
#         tmp = chr(x+65)
#     ans += chr(x+65) * (lst[x] // 2)
#
# lst_ans = list(ans)
# lst_ans.reverse()
# if check > 1:
#     print("I'm Sorry Hansoo")
# else:
#     print(ans + tmp + ''.join(map(str, lst_ans)))