import sys

n, k = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))

def selection_sort(arr, k):
    cnt = 0
    result = [0, 0]
    for i in range(len(arr)-1, -1, -1):
        tmp_arr = arr[:i+1]
        tmp, tmp_compare = arr[i], arr[tmp_arr.index(max(tmp_arr))]
        if tmp != tmp_compare:
            arr[i], arr[tmp_arr.index(max(tmp_arr))] = tmp_compare, tmp
            result[0] = min(tmp_compare, tmp)
            result[1] = max(tmp_compare, tmp)
            cnt += 1

        if cnt == k:
            print(*result)
            return

    print(-1)

selection_sort(num, k)