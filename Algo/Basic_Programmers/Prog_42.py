# 첫 번째로 나오는 음수

def solution(num_list):
    answer = -1

    for i in range(len(num_list)):
        if num_list[i] < 0:
            answer = i
            break

    return answer

print(solution([12, 4, 15, 46, 38, -2, 15]))
print(solution([13, 22, 53, 24, 15, 6]))