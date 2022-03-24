import sys

t = int(sys.stdin.readline())

for _ in range(t):
        num, unit = sys.stdin.readline().strip().split()

        if unit == 'kg':
            num = float(num) * float(2.2046)
            result = 'lb'
        elif unit == 'l':
            num = float(num) * float(0.2642)
            result = 'g'
        elif unit == 'lb':
            num = float(num) * float(0.4536)
            result = 'kg'
        else:
            num = float(num) * float(3.7854)
            result = 'l'

        print("{:.4f}".format(num), result)