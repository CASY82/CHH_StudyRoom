import sys

first = list(sys.stdin.readline().strip().split())
second = list(sys.stdin.readline().strip().split())
third = list(sys.stdin.readline().strip().split())

# 1번
tmp1 = [int(first[1]) % 100, int(second[1]) % 100, int(third[1]) % 100]
tmp1.sort()

# 2번
tmp2 = [[int(first[0]), first[2]], [int(second[0]), second[2]], [int(third[0]), third[2]]]
tmp2.sort(key=lambda x : x[0])


tmp1_res = ""
tmp2_res = ""

for a in range(3):
    tmp1_res += str(tmp1[a])

for b in range(3):
    tmp2_res += str(tmp2[b][1][0])

print(tmp1_res)
print(tmp2_res[::-1])