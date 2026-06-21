# 대문자와 소문자

def solution(n, t):
    answer = n

    for i in range(t):
        answer *= 2

    return answer

print(solution(2, 10))
print(solution(7, 15))