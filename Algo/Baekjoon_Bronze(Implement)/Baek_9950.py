import sys

while True:
    height, width, area = map(int, sys.stdin.readline().split())

    if height == width == area == 0:
        break

    if height == 0:
        height = area // width

    if width == 0:
        width = area // height

    if area == 0:
        area = height * width

    print(height, width, area)