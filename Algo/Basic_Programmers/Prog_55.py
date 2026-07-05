# 가까운 1 찾기

def solution(arr, idx):
    for i in range(idx, len(arr)):
        if arr[i] == 1:
            return i

    return -1

print(solution([0, 0, 0, 1], 1))
print(solution([1, 0, 0, 1, 0, 0], 4))
print(solution([1, 1, 1, 1, 0], 3))