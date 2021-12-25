import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())
    school = dict()

    for _ in range(n):
        name, beer = sys.stdin.readline().strip().split()

        school[int(beer)] = name

    a = sorted(school)
    print(school[a[-1]])