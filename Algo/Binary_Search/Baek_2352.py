#그냥 기본적인 LIS문제였다.
import sys

n = int(sys.stdin.readline())
line = list(map(int, sys.stdin.readline().split()))

new_line = [0]

for i in line:
    if new_line[-1] < i:
        new_line.append(i)
    else:
        start = 0
        end = len(new_line)

        while start < end:
            mid = (start + end) // 2

            if new_line[mid] < i:
                start = mid + 1
            else:
                end = mid

        new_line[end] = i

print(len(new_line)-1)