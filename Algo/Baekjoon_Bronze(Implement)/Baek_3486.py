import sys

t = int(sys.stdin.readline())

for _ in range(t):
    num1, num2 = sys.stdin.readline().strip().split()

    num1 = num1[::-1]
    num2 = num2[::-1]

    print(int(str(int(num1) + int(num2))[::-1]))