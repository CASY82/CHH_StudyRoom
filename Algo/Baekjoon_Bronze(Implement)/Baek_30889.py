import sys

n = int(sys.stdin.readline())
theater = [["." for _ in range(20)] for _ in range(10)]
alpha = "A B C D E F G H I J".split(" ")

for _ in range(n):
    seat = sys.stdin.readline().strip()

    theater[alpha.index(seat[0])][int(seat[1:]) - 1] = "o"

for i in range(10):
    for j in range(20):
        print(theater[i][j], end="")
    print()