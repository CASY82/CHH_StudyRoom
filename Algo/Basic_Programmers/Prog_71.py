# 원소들의 곱과 합
def solution(num_list):
    sum_tmp = sum(num_list) ** 2
    ggop_tmp = 1

    for i in num_list:
        ggop_tmp *= i

    if ggop_tmp < sum_tmp:
        return 1
    else:
        return 0

print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))
