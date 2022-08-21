import sys

while True:
    try:
        num = int(sys.stdin.readline())
    except:
        break

    one = '1'

    while True:
        if int(one) % num == 0:
            break

        one += '1'

    print(len(one))