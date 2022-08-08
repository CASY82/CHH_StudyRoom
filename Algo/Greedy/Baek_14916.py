import sys

n = int(sys.stdin.readline())

five = n // 5
result = False

while five >= 0:
    tmp = n

    tmp -= five * 5
    two = tmp // 2

    if tmp % 2 != 0:
        five -= 1
    else:
        result = True
        break

if result:
    print(two + five)
else:
    print(-1)