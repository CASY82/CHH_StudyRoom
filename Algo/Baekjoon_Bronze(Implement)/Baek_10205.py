import sys

t = int(sys.stdin.readline())

for cnt in range(t):
    head = int(sys.stdin.readline())
    act = list(sys.stdin.readline().strip())

    for i in range(len(act)):
        if act[i] == 'c':
            head += 1
        else:
            head -= 1

    print("Data Set {}:".format(cnt+1))
    print(head)
    print()