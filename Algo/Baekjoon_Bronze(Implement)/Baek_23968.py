import sys

n, k = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

#Bubble Sort
def bubbleSort(n, k):
    total_cnt = 0

    for i in range(n - 1, -1, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                total_cnt += 1

            if total_cnt == k:
                print(min(array[j], array[j + 1]), max(array[j], array[j + 1]))
                return total_cnt

    return -1

if bubbleSort(n, k) == -1:
    print(-1)