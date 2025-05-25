import sys

t = int(sys.stdin.readline())

for case in range(1, t + 1):
    ticket_num = int(sys.stdin.readline())

    ticket_list = list(map(int, sys.stdin.readline().split()))
    tmp_set = set(ticket_list)
    res = 0

    for i in tmp_set:
        if ticket_list.count(i) == 1:
            res = i

    print("Case #{0}: {1}".format(case, res))