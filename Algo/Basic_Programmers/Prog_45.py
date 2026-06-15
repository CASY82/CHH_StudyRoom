# 숫자 찾기

def solution(start_num, end_num):
    answer = []
    for i in range(start_num, end_num + 1):
        answer.append(i)

    return answer

print(solution(3, 10))