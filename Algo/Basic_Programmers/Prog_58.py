def solution(i, j, k):
    tmp = ""

    for num in range(i, j + 1):
        tmp = tmp + str(num)

    return tmp.count(str(k))

print(solution(1, 13, 1))
print(solution(10, 50, 5))
print(solution(3, 10, 2))
