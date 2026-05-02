# 특정 문자열로 끝나는 가장 긴 부분 문자열 찾기

# def solution(myString, pat):
#     tmp = []
#     res = []
#     index = 0
#
#     for i in range(len(myString)):
#         if pat[index] == myString[i]:
#             index += 1
#         else:
#             index = 0
#
#         tmp.append(myString[i])
#
#         # append를 문자 추가/매칭 처리 후에 해야 함
#         if index == len(pat):
#             res.append("".join(tmp))
#             index = 0
#
#     return res[-1]

def solution(myString, pat):
    idx = myString.rfind(pat)
    return myString[:idx + len(pat)]

print(solution("AbCdEFG", "dE"))
print(solution("AAAAaaaa", "a"))