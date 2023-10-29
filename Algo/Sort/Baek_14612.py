import sys

n, m = map(int, sys.stdin.readline().split())

orders = []

for _ in range(n):
    command = list(sys.stdin.readline().strip().split())

    if command[0] == "order":
        table = int(command[1])
        time = int(command[2])
        orders.append((table, time))
    elif command[0] == "sort":
        orders.sort(key=lambda x: (x[1], x[0]))
    else:
        delete = int(command[1])
        for i in range(len(orders)):
            if delete == orders[i][0]:
                orders.pop(i)
                break

    if len(orders) == 0:
        print("sleep")
    else:
        for order in range(len(orders)):
            if order < len(orders) - 1:
                print(orders[order][0], end=" ")
            else:
                print(orders[order][0])