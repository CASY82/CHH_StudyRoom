# Extreme Temperatures
import sys

min_num = 999999999
max_num = -999999999

for line in sys.stdin:
    data = line.split()

    tmp = data[1:]
    nums = []
    for i in range(len(tmp)):
        nums.append(int(tmp[i]))

    tmp_max = max(nums)
    tmp_min = min(nums)

    max_num = max(max_num, tmp_max)
    min_num = min(min_num, tmp_min)

print(min_num, max_num)