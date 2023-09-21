import sys

white = "K P N B R Q".split(" ")
black = "k p n b r q".split(" ")

score = [0, 1, 3, 3, 5, 9]

result = 0

for i in range(8):
    chess = sys.stdin.readline().strip()

    for checking in range(8):
        if chess[checking] in white:
            result += score[white.index(chess[checking])]
        elif chess[checking] in black:
            result -= score[black.index(chess[checking])]

print(result)