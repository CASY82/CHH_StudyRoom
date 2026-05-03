# 문자열이 몇 번 등장하는지 세기

def solution(myString, pat):
    res = 0
    for i in range(len(myString) - (len(pat) - 1)):
        if myString[i:i + len(pat)] == pat:
            res += 1

    return res

print(solution("banana", "ana"))
print(solution("aaaa", "aa"))