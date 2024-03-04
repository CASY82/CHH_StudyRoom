import sys

m = int(sys.stdin.readline())

total = 0
xor = 0

for _ in range(m):
    command = list(sys.stdin.readline().strip().split())

    if command[0] == "1":
        total += int(command[1])
        xor ^= int(command[1])

    if command[0] == "2":
        total -= int(command[1])
        xor ^= int(command[1])

    if command[0] == "3":
        print(total)

    if command[0] == "4":
        print(xor)