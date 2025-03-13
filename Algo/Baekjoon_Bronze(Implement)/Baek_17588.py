import sys

n = int(sys.stdin.readline())
nums = []

for _ in range(n):
    nums.append(int(sys.stdin.readline()))

nums.sort()
res = []

for i in range(1, nums[-1] + 1):
    if i not in nums:
        res.append(i)

if len(res) >= 1:
    for j in range(len(res)):
        print(res[j])
else:
    print("good job")