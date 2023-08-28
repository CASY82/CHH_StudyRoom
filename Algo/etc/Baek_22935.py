import sys

t = int(sys.stdin.readline())
num_arr_under_29 = "1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1".split(" ")
num_arr_over_29 = "2 3 4 5 6 7 8 9 10 11 12 13 14 15 14 13 12 11 10 9 8 7 6 5 4 3 2 1".split(" ")

for _ in range(t):
    num = int(sys.stdin.readline())

    if num <= 29:
        tmp = format(int(num_arr_under_29[(num - 1) % 29]), '04b')
    else:
        tmp = format(int(num_arr_over_29[(num - 30) % 28]), '04b')

    result = ""

    for point in range(len(tmp)):
        if tmp[point] == "1":
            result += "딸기"
        else:
            result += "V"

    print(result)