# 등차수열의 특정한 항만 더하기
def solution(a, d, included):
    answer = 0

    for i in range(len(included)):
        if included[i]:
            answer += (a + i * d)

    return answer

print(solution(3, 4, [True, False, False, True, True]))
