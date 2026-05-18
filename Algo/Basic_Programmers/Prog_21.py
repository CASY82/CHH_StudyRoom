# 카운트 다운

def solution(start_num, end_num):
    answer = []

    for i in range(start_num, end_num - 1, -1):
        answer.append(i)

    return answer

print(solution(10, 3))