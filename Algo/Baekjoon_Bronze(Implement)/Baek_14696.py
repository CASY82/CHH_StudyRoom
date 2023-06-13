import sys

n = int(sys.stdin.readline())

for _ in range(n):
    a_list = list(map(int, sys.stdin.readline().split()))
    b_list = list(map(int, sys.stdin.readline().split()))

    a_list = a_list[1:]
    b_list = b_list[1:]

    a_dic = {4: 0, 3: 0, 2: 0, 1: 0}
    b_dic = {4: 0, 3: 0, 2: 0, 1: 0}

    for a in a_list:
        a_dic[a] += 1

    for b in b_list:
        b_dic[b] += 1

    draw = False

    for num in range(4, 0, -1):
        if a_dic[num] > b_dic[num]:
            print("A")
            break
        elif a_dic[num] < b_dic[num]:
            print("B")
            break
        else:
            if num == 1:
                draw = True

    if draw:
        print("D")