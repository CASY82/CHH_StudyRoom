import sys

def thue_morse(k):
    n = k - 1
    ones = bin(n).count('1')
    return '1' if (ones % 2) else '0'

k = int(sys.stdin.readline())

print(thue_morse(k))