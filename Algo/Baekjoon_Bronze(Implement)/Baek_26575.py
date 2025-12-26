import sys
from decimal import Decimal, ROUND_HALF_UP

n = int(sys.stdin.readline())

for _ in range(n):
    d, f, p = sys.stdin.readline().split()

    d = Decimal(d)
    f = Decimal(f)
    p = Decimal(p)

    total = (d * f * p).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
    print(f"${total}")