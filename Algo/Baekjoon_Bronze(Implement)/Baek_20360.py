import sys

n = int(sys.stdin.readline())

tmp_binary = bin(n)
binary = tmp_binary[2:]
binary = binary[::-1]
for num in range(len(binary)):
    if int(binary[num]) == 1:
        print(num, end=" ")