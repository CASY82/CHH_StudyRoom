# flag에 따라 다른 값 반환하기

def solution(a, b, flag):
    if flag:
        return a + b
    else:
        return a - b

print(solution(-4, 7, True))
print(solution(-4, 7, False))