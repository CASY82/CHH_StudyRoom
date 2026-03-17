# X X glued
import sys

while True:
    data = sys.stdin.readline().strip().split()

    if data[0] == "#":
        break

    tmp = []

    for i in range(1, 4):
        if data[1][i-1] == data[1][i]:
            if data[1][i] not in tmp:
                tmp.append(data[1][i])

    if len(tmp) == 2:
        print(f"{tmp[0]} {tmp[0]} glued and {tmp[1]} {tmp[1]} glued")
    elif len(tmp) == 1:
        print(f"{tmp[0]} {tmp[0]} glued")