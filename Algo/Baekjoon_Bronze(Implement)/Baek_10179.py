import sys

t = int(sys.stdin.readline())

for _ in range(t):
    price = float(sys.stdin.readline())
    price = round(price * 0.8, 2)

    print("${:.2f}".format(price))