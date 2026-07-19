# 홀수 vs 짝수
def solution(num_list):
    odd = 0
    even = 0

    for i in range(1, len(num_list) + 1):
        if i % 2 == 0:
            even += num_list[i - 1]
        else:
            odd += num_list[i - 1]

    return max(even, odd)