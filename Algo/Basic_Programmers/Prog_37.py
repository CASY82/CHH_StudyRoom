# 배열 만들기 1

def solution(n, k):
    answer = []

    for i in range(0, n + 1, k):
        answer.append(i)

    return answer[1:]

print(solution(10, 3))
print(solution(15, 5))