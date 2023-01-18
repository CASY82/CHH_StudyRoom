import sys

def GCD(a, b):
    if a % b == 0:
        return b
    else:
        return GCD(b, a%b)

n = int(sys.stdin.readline())
origin_tree = []

for _ in range(n):
    origin_tree.append(int(sys.stdin.readline()))

origin_tree.sort()

diff = []

for i in range(1, len(origin_tree)):
    diff.append(origin_tree[i] - origin_tree[i-1])

tmp = list(set(diff))
interval = GCD(diff[0], diff[1])

for j in range(2, len(diff)):
    interval = GCD(diff[j], interval)

result = 0

for k in diff:
    result += k // interval - 1

print(result)

# tmp = min(origin_tree)
# result = []
#
# while tmp < max(origin_tree):
#     if tmp not in origin_tree:
#         result.append(tmp)
#
#     tmp += interval
#
# print(len(result))