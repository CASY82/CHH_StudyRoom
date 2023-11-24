import sys

n, l = map(int, sys.stdin.readline().split())
max_black = 0
zebra_cnt = 0
zebra_data = []

def compress_string(string):
    compressed = string[0]

    for i in range(1, len(string)):
        if string[i] != string[i - 1]:
            compressed += string[i]

    return compressed

for _ in range(n):
    zebra = list(sys.stdin.readline().strip())

    black_stripe = 0
    compress_zebra = compress_string(zebra)

    zebra_data.append(compress_zebra.count('1'))

max_black = max(zebra_data)
zebra_cnt = zebra_data.count(max_black)

print(max_black, zebra_cnt)