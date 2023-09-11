import sys

while True:
    income = int(sys.stdin.readline())

    if income == 0:
        break

    if income <= 1000000:
        print(income)
    elif 1000000 < income <= 5000000:
        print(int(income - (income * 0.1)))
    elif 5000000 < income :
        print(int(income - (income * 0.2)))