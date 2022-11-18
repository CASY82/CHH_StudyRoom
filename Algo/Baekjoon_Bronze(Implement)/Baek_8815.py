import sys

arr = "A B C B C D C D A D A B".split(" ")
z = int(sys.stdin.readline())

for _ in range(z):
    n = int(sys.stdin.readline())

    print(arr[(n-1) % 12])