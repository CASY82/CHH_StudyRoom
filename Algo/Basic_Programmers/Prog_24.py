# 리스트 자르기

def solution(n, slicer, num_list):
    answer = []

    if n == 1:
        return num_list[:slicer[1] + 1]
    elif n == 2:
        return num_list[slicer[0]:]
    elif n == 3:
        return num_list[slicer[0]:slicer[1] + 1]
    elif n == 4:
        for i in range(slicer[0], slicer[1] + 1, slicer[2]):
            answer.append(num_list[i])

        return answer

print(solution(3, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(solution(4, [1, 5, 2], [1, 2, 3, 4, 5, 6, 7, 8, 9]))