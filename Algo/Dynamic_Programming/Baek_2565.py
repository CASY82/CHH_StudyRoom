import sys

n = int(sys.stdin.readline())

elec = []

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    elec.append((a, b))

elec.sort(key=lambda x: x[0])
tmp = []

for line in elec:
    tmp.append(line[1])

# print(tmp)

length = len(tmp)
# reverse_tmp = list(reversed(tmp))

dp = [1 for _ in range(length)]
# dp_down = [1 for _ in range(length)]
# rev_dp = [1 for _ in range(length)]
# rev_dp_down = [1 for _ in range(length)]

for i in range(length):
    for j in range(i):
        if tmp[i] > tmp[j]:
            dp[i] = max(dp[i], dp[j] + 1)

        # if tmp[i] < tmp[j]:
        #     dp_down[i] = max(dp_down[i], dp_down[j] + 1)
        #
        # if reverse_tmp[i] > reverse_tmp[j]:
        #     rev_dp[i] = max(rev_dp[i], rev_dp[j] + 1)
        #
        # if reverse_tmp[i] < reverse_tmp[j]:
        #     rev_dp_down[i] = max(rev_dp_down[i], rev_dp_down[j] + 1)

# print(rev_dp, dp, rev_dp_down, dp_down)

print(length - max(dp))
# print(min(length - max(rev_dp), length - max(dp)))