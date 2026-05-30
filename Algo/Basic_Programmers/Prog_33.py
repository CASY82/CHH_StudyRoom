# 문자열 곱하기

def solution(my_string, k):
    answer = ''

    for _ in range(k):
        answer += my_string

    return answer

print(solution("string", 3))
print(solution("love", 10))