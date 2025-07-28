import sys

n, m, b = map(int, sys.stdin.readline().split())

freq = [0] * 257
for _ in range(n):
    for h in map(int, sys.stdin.readline().split()):
        freq[h] += 1

    total_cells = n * m

    pre_cnt = [0] * 257
    pre_sum = [0] * 257

    pre_cnt[0] = freq[0]
    pre_sum[0] = 0 * freq[0]

    for h in range(1, 257):
        pre_cnt[h] = pre_cnt[h - 1] + freq[h]
        pre_sum[h] = pre_sum[h - 1] + h * freq[h]

    total_sum = pre_sum[256]

    best_time = float('inf')
    best_h = 0

    for H in range(257):
        if H > 0:
            need = H * pre_cnt[H - 1] - pre_sum[H - 1]
        else:
            need = 0

        remove = (total_sum - pre_sum[H]) - H * (total_cells - pre_cnt[H])

        if b + remove < need:
            continue

        time = 2 * remove + need

        if time < best_time or (time == best_time and H > best_h):
            best_time = time
            best_h = H

print(best_time, best_h)