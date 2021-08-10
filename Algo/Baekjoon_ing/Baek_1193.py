#수열의 패턴을 확인한 뒤, 해당 수학 공식들을 이용하여 범위를 구한다.
X = int(input())
i = 1
mid_num = 0
ai = []

while True:
    if X > ((i - 1) * i // 2) and X <= ((i + 1) * i // 2):
        mid_num = i
        break

    i += 1

X = X - ((mid_num - 1) * mid_num // 2)


for i in range(mid_num):
    ai.append(f'{i + 1}/{mid_num - i}')


if mid_num % 2 == 0:
    print(ai[X-1])
else:
    print(ai[(mid_num-1) - (X - 1)])


#다른사람 풀이

# X = int(input())
#
# line = 1
# while X > line:
#     X -= line
#     line += 1
#
# if line % 2 == 0:
#     a = X
#     b = line - X + 1
# else:
#     a = line - X + 1
#     b = X
#
# print(a, '/', b, sep='') #핵심은 이 부분을 문자열처럼 해서 구한다는 점... 나는 너무 어렵게 구했다.