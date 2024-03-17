import sys

a, c, e = map(int, sys.stdin.readline().split())
get_a, get_c, get_e = map(int, sys.stdin.readline().split())

if get_e >= e:
    if (c + 1) // 2 <= get_c < c:
        print("D")
    elif get_c >= c:
        if (a + 1) // 2 <= get_a < a:
            print("B")
        elif a <= get_a:
            print("A")
        else:
            print("C")
    else:
        print("E")