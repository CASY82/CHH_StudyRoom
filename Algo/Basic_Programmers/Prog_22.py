# 글자 지우기

def solution(my_string, indices):
    answer = ''
    indices.sort()
    index = 0

    for i in range(len(my_string)):
        if index < len(indices) and indices[index] == i:
            index += 1
        else:
            answer = answer + my_string[i]

    return answer

print(solution("apporoograpemmemprs", [1, 16, 6, 15, 0, 10, 11, 3]))