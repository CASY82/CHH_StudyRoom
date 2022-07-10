import sys

while True:
    a, b = sys.stdin.readline().split()

    if a == '0' and b == '0':
        break

    cnt = 0

    a_list = list(a)
    b_list = list(b)

    short = min(len(a_list), len(b_list))
    long = max(len(a_list), len(b_list))
    case = False

    for i in range(long):
        if i < short:
            if case:
                tmp = int(a_list[-i - 1]) + int(b_list[-i - 1]) + 1
            else:
                tmp = int(a_list[-i - 1]) + int(b_list[-i - 1])
        else:
            if len(a_list) > len(b_list):
                tmp = int(a_list[-i - 1]) + 1
            else:
                tmp = int(b_list[-i - 1]) + 1

        if tmp >= 10:
            case = True
            cnt += 1
        else:
            case = False

    print(cnt)