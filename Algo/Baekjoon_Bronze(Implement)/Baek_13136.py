r, c, n = map(int, input().split())

if r % n == 0 and c % n == 0:
    print((r // n) * (c // n))
else:
    if r % n != 0 and c % n == 0:
        print(((r // n) + 1) * (c // n))
    elif c % n != 0 and r % n == 0:
        print((r // n) * ((c // n) + 1))
    else:
        print(((r // n) + 1) * ((c // n) + 1))