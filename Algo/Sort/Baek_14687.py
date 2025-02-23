import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

if n % 2 != 0:
    lows = nums[:n // 2 + 1]
    highs = nums[n // 2 + 1:]
else:
    lows = nums[:n // 2]
    highs = nums[n // 2:]

lows.reverse()
res = []

for i in range(len(highs)):
    res.append(lows[i])
    res.append(highs[i])

if len(lows) > len(highs):
    res.append(lows[-1])

print(*res)

#다른 사람 풀이
# n,*a = map(int,open(0).read().split())
# a.sort()
# b = [0]*n
# b[::2] = a[:(n+1)//2][::-1]
# b[1::2] = a[(n+1)//2:]
# print(*b)