import sys

k = int(sys.stdin.readline())

for i in range(k):
    forecast, real = map(int, sys.stdin.readline().split())

    print("Data Set {}:".format(i+1))

    if forecast <= real:
        print("no drought")
    else:
        i = 0
        while True:
            if real < forecast <= real * 5:
                break
            else:
                i += 1
                real *= 5

        for j in range(i):
            print("mega ", end="")
        print("drought")

    print()