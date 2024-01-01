import sys

t = int(sys.stdin.readline())

def find_dice_combinations(sum_value):
    combinations = []
    for die1 in range(1, 7):
        die2 = sum_value - die1
        if 1 <= die2 <= 6:
            combinations.append((die1, die2))

    length = len(combinations)

    if length % 2 == 0:
        combinations = combinations[:length // 2]
    else:
        combinations = combinations[:length // 2 + 1]

    return combinations

for i in range(t):
    square_sum = int(sys.stdin.readline())

    print("Case {}:".format(i + 1))

    tmp = find_dice_combinations(square_sum)

    for j in range(len(tmp)):
        print("({0},{1})".format(tmp[j][0], tmp[j][1]))

# import sys
#
# t = int(sys.stdin.readline())
#
# for i in range(t):
#     sqaure_sum = int(sys.stdin.readline())
#
#     print(f"Case {i + 1}:")
#
#     for a in range(1, 7):
#         for b in range(a, 7):
#             if a + b == sqaure_sum:
#                 print(f"({a},{b})")