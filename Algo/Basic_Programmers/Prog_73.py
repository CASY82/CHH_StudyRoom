# 특이한 정렬
def solution(numlist, n):
    tmp = []

    for num in numlist:
        tmp.append([num, abs(num - n)])

    tmp.sort(key=lambda x: (x[1], -x[0]))

    return [x[0] for x in tmp]

print(solution([1, 2, 3, 4, 5, 6], 4))
print(solution([10000,20,36,47,40,6,10,7000], 30))