# 길이에 따른 연산

def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    else:
        tmp = 1
        for num in num_list:
            tmp *= num
        return tmp

print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))
print(solution([2, 3, 4, 5]))