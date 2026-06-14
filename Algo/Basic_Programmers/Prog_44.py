# 숫자 찾기

def solution(num, k):
    tmp = list(str(num))

    try:
        ans = tmp.index(str(k)) + 1
    except:
        ans = -1

    return ans

print(solution(29183, 1))
print(solution(232443, 4))
print(solution(123456, 7))