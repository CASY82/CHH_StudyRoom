n = 12345

def solution(n):
    result = list(map(int, str(n)))
    result.reverse()

    return result

print(solution(n))
