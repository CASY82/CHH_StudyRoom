# 2의 영역

def solution(arr):
    tmp = []

    for i in range(len(arr)):
        if arr[i] == 2:
            tmp.append(i)

    if tmp:
        return arr[tmp[0]:tmp[-1] + 1]
    else:
        return [-1]

print(solution([1, 2, 1, 4, 5, 2, 9]))
print(solution([1, 2, 1]))
print(solution([1, 1, 1]))
print(solution([1, 2, 1, 2, 1, 10, 2, 1]))