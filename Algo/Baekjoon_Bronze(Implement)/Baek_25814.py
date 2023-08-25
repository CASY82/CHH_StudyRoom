import sys

def weight_calculate(num):
    str_num = str(num)
    length = len(str_num)
    pos_sum = 0
    for pos in range(length):
        pos_sum += int(str_num[pos])

    return length * pos_sum

first, second = map(int, sys.stdin.readline().split())

fir = weight_calculate(first)
sec = weight_calculate(second)

if fir > sec:
    print(1)
elif fir < sec:
    print(2)
else:
    print(0)