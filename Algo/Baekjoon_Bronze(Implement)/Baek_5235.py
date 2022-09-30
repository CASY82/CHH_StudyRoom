import sys

t = int(sys.stdin.readline())

for _ in range(t):
    num_list = list(map(int, sys.stdin.readline().split()))

    even_sum = 0
    odd_sum = 0

    for num in range(1, len(num_list)):
        if num_list[num] % 2 == 0:
            even_sum += num_list[num]
        else:
            odd_sum += num_list[num]

    if even_sum > odd_sum:
        print("EVEN")
    elif odd_sum > even_sum:
        print("ODD")
    else:
        print("TIE")