import sys
import math

n = int(sys.stdin.readline())

tmp = 1 - (4 * (1 - n))
result_plus = ((-1) + math.sqrt(tmp)) // 2
result_minus = ((-1) - math.sqrt(tmp)) // 2

print(max(int(result_plus), int(result_minus)))