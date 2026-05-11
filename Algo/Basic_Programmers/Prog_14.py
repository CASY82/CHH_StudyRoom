# 조건에 맞게 수열 변환하기 2

def solution(arr):
    answer = 0
    start = arr.copy()
    next = []

    while True:
        for num in start:
            if num >= 50 and num % 2 == 0:
                num //= 2
            elif num < 50 and num % 2 == 1:
                num = num * 2 + 1

            next.append(num)

        if start == next:
            return answer
        else:
            answer += 1
            start = next.copy()
            next = []

print(solution([1, 2, 3, 100, 99, 98]))