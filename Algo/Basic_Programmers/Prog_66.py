# 제곱수 판별하기
import math

def solution(n):
    if math.sqrt(n) == int(math.sqrt(n)):
        return 1
    else:
        return 2

print(solution(144))
print(solution(976))
