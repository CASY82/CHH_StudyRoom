import sys

while True:
    bus, passenger = sys.stdin.readline().split()

    if bus == "#" and passenger == "0":
        break

    passenger = int(passenger)
    in_bus = int(sys.stdin.readline())
    bus_stop = int(sys.stdin.readline())

    for _ in range(bus_stop):
        outer, inner = map(int, sys.stdin.readline().split())

        if in_bus - outer < 0:
            in_bus = 0
        else:
            in_bus -= outer

        if in_bus + inner > passenger:
            in_bus = passenger
        else:
            in_bus += inner

    print(bus, in_bus)