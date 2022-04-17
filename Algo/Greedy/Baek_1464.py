# import sys
#
# word = sys.stdin.readline().strip()

# for i in range(1, len(word)):
#     tmp = word[i::-1]+word[i+1:]
#
#     if tmp < word:
#         print(tmp)

import sys
from collections import deque

word = sys.stdin.readline().strip()
que = deque()

que.append(word[0])

for i in range(1, len(word)):
    if word[i] < que[-1]:
        if word[i] > que[0]:
            que.append(word[i])
        else:
            que.appendleft(word[i])
    else:
        que.append(word[i])

for i in que:
    print(i, end='')

# 다른사람 풀이
# import sys
# s=sys.stdin.readline().rstrip()
# for i in range(1,len(s)-1):
#     if s[0]>=s[i+1]:
#         if s[i]>s[0] or s[i]<s[i+1]:
#             s=s[i::-1]+s[i+1:]
#     else:
#         if s[i]<s[0]:
#             s=s[i::-1]+s[i+1:]
# print(s if s[0]<=s[-1] else s[::-1])

# 다른사람 풀이 2
# t = input()
#
#
# for i in range(len(t)-1):
#     if t[i]<t[i+1]:
#         temp = t[:i+1]
#         temp = temp[::-1]
#         t = temp+t[i+1:]
#         temp = t[:i+2]
#         temp = temp[::-1]
#         t = temp+t[i+2:]
# print(t[::-1])