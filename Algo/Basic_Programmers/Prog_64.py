# 홀짝에 따라 다른 값 반환하기

def solution(n):
    answer = 0

    if n % 2 == 1:
        for i in range(n + 1):
            if i % 2 == 1:
                answer += i
    else:
        for i in range(n + 1):
            if i % 2 == 0:
                answer += i * i

    return answer

print(solution(7))
print(solution(10))
