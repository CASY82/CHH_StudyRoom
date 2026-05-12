# 조건에 맞게 수열 변환하기 1

def solution(arr):
    answer = []

    for num in arr:
        if num >= 50 and num % 2 == 0:
            num //= 2
        elif num < 50 and num % 2 == 1:
            num *= 2

        answer.append(num)

    return answer

print(solution([1, 2, 3, 100, 99, 98]))