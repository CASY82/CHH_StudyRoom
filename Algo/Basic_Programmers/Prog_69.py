# 공배수
def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1

    return 0

print(solution(60, 2, 3))
print(solution(55, 10, 5))
