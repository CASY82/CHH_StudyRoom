# import sys
#
# susic = sys.stdin.readline().strip()
# num = ''
# mathEx = []
#
# for i in range(len(susic)):
#     if ord(susic[i]) >= ord('0') and ord(susic[i]) <= ord('9'):
#         num += susic[i]
#     else:
#         tmp = int(num)
#         num = ''
#         mathEx.append(tmp)
#         mathEx.append(susic[i])
#
# tmp = int(num)
# mathEx.append(tmp)
#
# print(mathEx)

import sys

susic = sys.stdin.readline().strip()
num = ''
mathEx = []

#리스트로 분리
for i in range(len(susic)):
    if ord('0') <= ord(susic[i]) <= ord('9'):
        num += susic[i]
    else:
        mathEx.append(str(int(num)))
        mathEx.append(susic[i])
        num = ''
mathEx.append(str(int(num)))

i = len(mathEx)-1
#'+'연산을 일단 다 한다.
while mathEx.count('+') != 0:
    if i == 0:
        break

    if mathEx[i] == '+':
        a = int(mathEx.pop(i+1))
        mathEx.pop(i)
        b = int(mathEx.pop(i-1))
        mathEx.insert(i-1, str(a + b))

    i -= 1

#'-' 연산을 끝낸다.
print(eval(''.join(mathEx)))

#좀더 간단히 생각할 수 있는 split을 이용한 방법을 찾았다...
# import sys
#
# a = sys.stdin.readline().split('-')
# val = []
# for i in a:
#     cnt = 0
#     s = i.split('+')
#     for j in s:
#         cnt += int(j)
#     val.append(cnt)
# rsl = val[0]
# for i in val[1:]:
#     rsl -= i
# print(rsl)

#2번 예제 더 짧아서 가져왔다.
# n = input().split('-')
#
# sum = 0
#
# for i in n[0].split('+'):  # -가 있기 전
#     sum += int(i)
#
# for i in n[1:]:
#     for j in i.split('+'):
#         sum -= int(j)
#
# print(sum)