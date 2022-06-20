import sys

t = int(sys.stdin.readline())

for _ in range(t):
    binary_one, binary_two = sys.stdin.readline().strip().split()

    counter_one = binary_one.count('1')
    counter_two = binary_two.count('1')
    mover = 0
    changer = abs(counter_one - counter_two)

    for i in range(len(binary_one)):
        if binary_one[i] == '1' and binary_one[i] == binary_two[i]:
            mover += 1

    print(abs(min(counter_one, counter_two) - mover) + changer)