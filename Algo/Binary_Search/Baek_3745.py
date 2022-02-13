import sys

def lis(arr):
    new_arr = [0]

    for i in arr:
        if new_arr[-1] < i:
            new_arr.append(i)
        else:
            start = 0
            end = len(new_arr)

            while start < end:
                mid = (start + end) // 2

                if new_arr[mid] < i:
                    start = mid + 1
                else:
                    end = mid

            new_arr[end] = i

    return len(new_arr)-1

while True:
    try:
        n = int(sys.stdin.readline())
    except:
        break

    juga = list(map(int, sys.stdin.readline().split()))

    print(lis(juga))