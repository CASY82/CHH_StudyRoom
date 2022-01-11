import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    exPay = 0
    exPlayer = ''
    for _ in range(n):
        pay, player = sys.stdin.readline().strip().split()

        if int(pay) > exPay:
            exPay = int(pay)
            exPlayer = player

    print(exPlayer)
