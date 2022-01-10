# import sys

# 길이가 긴 단어의 제일 큰자리수 순서대로 큰값 부여 ==> 길이가 같다면 번갈아 가면서...
# 짧은 쪽 단어에 그 다음 순서대로 큰값 부여
# 즉 단어가 나오는 순서중 작은놈을 해당 알파벳과 매칭하고(큰쪽은 무시해도됨) 작은 순서대로 아무렇게나 9부터 0까지 배열하면됨
# 인줄 알았으나 반례가 존재해버렸다...
# 10
# ABB
# BB
# BB
# BB
# BB
# BB
# BB
# BB
# BB
# BB

# n = int(sys.stdin.readline())
#
# word = []
# alpha = dict()
# changeRS = []
# result = 0
#
# for _ in range(n):
#     word.append(sys.stdin.readline().strip())
#
# word.sort(key=lambda x:len(x), reverse=True)
#
# for i in word:
#     for j in range(len(i)):
#         if i[j] not in alpha:
#             alpha[i[j]] = len(i) - j
#         else:
#             if alpha[i[j]] < (len(i) - j):
#                 alpha[i[j]] = len(i) - j
#
# # 알파벳 우선순위 주고
# alphaP = sorted(alpha.items(), key=lambda x:x[1], reverse=True)
#
# # 우선순위에 따른 숫자 배정
# numChange = dict()
# for i in range(len(alphaP)):
#     numChange[alphaP[i][0]] = str(9-i)
#
# print(numChange)
#
# # 문자열을 수로 변환한 뒤 덧셈연산하면 끝
# for i in word:
#     tmp = ''
#     for j in range(len(i)):
#         tmp += numChange[i[j]]
#
#     result += int(tmp)
#
# print(result)

# 힌트를 얻어서 풀었지만 구현 자체는 직접함
import sys

n = int(sys.stdin.readline())

word = []
alpha = dict()
changeRS = []
result = 0

for _ in range(n):
    word.append(sys.stdin.readline().strip())

word.sort(key=lambda x:len(x), reverse=True)
# 알파벳 우선순위 지정 각 자리수의 합을 기준으로 우선순위 지정(반례를 의식함)
for i in word:
    for j in range(len(i)):
        if i[j] not in alpha:
            alpha[i[j]] = 10 ** (len(i) - j - 1)
        else:
            alpha[i[j]] += 10 ** (len(i) - j - 1)

alphaP = sorted(alpha.items(), key=lambda x:x[1], reverse=True)

# 우선순위에 따른 숫자 배정
numChange = dict()
for i in range(len(alphaP)):
    numChange[alphaP[i][0]] = str(9-i)

# 문자열을 수로 변환한 뒤 덧셈연산하면 끝
for i in word:
    tmp = ''
    for j in range(len(i)):
        tmp += numChange[i[j]]

    result += int(tmp)

print(result)