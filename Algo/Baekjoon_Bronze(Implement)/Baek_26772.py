import sys

n = int(sys.stdin.readline())

heart_lines = [
        " @@@   @@@  ",
        "@   @ @   @ ",
        "@    @    @ ",
        "@         @ ",
        " @       @  ",
        "  @     @   ",
        "   @   @    ",
        "    @ @     ",
        "     @      "
    ]


for i in range(len(heart_lines)):
    for _ in range(n):
        print(heart_lines[i], end="")
    print()