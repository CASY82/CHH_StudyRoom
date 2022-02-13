import sys

n = int(sys.stdin.readline())
electric_line = list(map(int, sys.stdin.readline().split()))

keep_line = [0]

for i in electric_line:
    if keep_line[-1] < i:
        keep_line.append(i)
    else:
        start = 0
        end = len(keep_line)

        while start < end:
            mid = (start + end) // 2

            if keep_line[mid] <= i:
                start = mid + 1
            else:
                end = mid

        keep_line[end] = i

print(n - (len(keep_line)-1))