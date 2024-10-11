import sys

#간단히 조합을 사용하면 풀 수 있는 문제
def factorial(x):
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x + 1):
        result *= i
    return result

def combinations(n, r):
    if n < r:
        return 0
    return factorial(n) // (factorial(r) * factorial(n - r))

def count_combinations(n):
    # n에서 4개의 수를 선택할 때, 가장 큰 수가 마지막에 오는 경우의 수
    if n < 4:
        return 0
    return combinations(n - 1, 3)  # 가장 큰 수를 제외한 나머지 3개를 선택

n = int(sys.stdin.readline())
result = count_combinations(n)
print(result)