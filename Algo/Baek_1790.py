import sys

def kth_digit(N, k):
    start = 1
    digits = 1
    while start <= N:
        end = min(N, 10**digits - 1)
        cnt = end - start + 1
        block_len = cnt * digits
        if k <= block_len:
            offset = (k - 1) // digits
            idx_in_num = (k - 1) % digits
            target = start + offset
            return int(str(target)[idx_in_num])
        k -= block_len
        digits += 1
        start *= 10

    return -1

data = sys.stdin.readline().strip().split()
N = int(data[0]); k = int(data[1])
print(kth_digit(N, k))