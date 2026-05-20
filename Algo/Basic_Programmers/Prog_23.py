# 덧칠하기

def solution(n, m, section):
    answer = 0
    end = 0

    for i in section:
        if i > end:
            answer += 1
            end = i + m - 1

    return answer

print(solution(8, 4, [2, 3, 6]))
print(solution(5, 4, [1, 3]))
print(solution(4, 1, [1, 2, 3, 4]))