# 길이에 따른 연산

def solution(num_list):
    answer = 0

    for num in num_list:
        tmp = num
        while tmp > 1:
            if tmp % 2 == 0:
                tmp //= 2
            else:
                tmp = (tmp - 1) // 2

            answer += 1

    return answer

print(solution([12, 4, 15, 1, 14]))