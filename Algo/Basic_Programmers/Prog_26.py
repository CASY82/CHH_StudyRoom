# 더 크게 합치기

def solution(a, b):
    return max(int(str(a) + str(b)), int(str(b) + str(a)))

print(solution(9, 91))
print(solution(89, 8))