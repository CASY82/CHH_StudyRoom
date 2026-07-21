# 두 수의 연산값 비교하기

def solution(a, b):
    plus = int(str(a) + str(b))
    tmp = 2 * a * b

    return max(plus, tmp)

print(solution(2, 91))
print(solution(91, 2))
