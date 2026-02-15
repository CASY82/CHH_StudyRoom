# 포도주 시음
import sys

def bottom_sum(m: int) -> int:
    return pref[m]

def top_sum(m: int) -> int:
    return total - pref[n - m]

n, k = map(int, sys.stdin.readline().split())
t = list(map(int, sys.stdin.readline().split()))

t.sort()

# 누적합 구하기
pref = [0] * (n + 1)
for i, x in enumerate(t, 1):
    pref[i] = pref[i - 1] + x

total = pref[n]

max_g = (k - 1) // 2
ans = 0

for g in range(max_g + 1):
    val = top_sum(g + 1) - bottom_sum(g)
    if val > ans:
        ans = val

print(ans)