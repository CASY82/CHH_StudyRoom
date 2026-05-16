# 왼쪽 오른쪽

def solution(num_list, n):
    answer = num_list[n:]
    answer = answer + num_list[:n]

    return answer

print(solution([2, 1, 6], 1))
print(solution([5, 2, 1, 7, 5], 3))