import sys

n = int(sys.stdin.readline())
tickets = list(map(int, sys.stdin.readline().split()))

tickets.sort()
my_ticket = 1

for i in range(n):
    if tickets[i] > my_ticket:
        break

    my_ticket += 1

print(my_ticket)