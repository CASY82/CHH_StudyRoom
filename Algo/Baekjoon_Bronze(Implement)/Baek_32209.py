import sys

q = int(sys.stdin.readline())
question = 0
res = True

for _ in range(q):
    command, value = sys.stdin.readline().strip().split()

    if command == "1":
        question += int(value)
    else:
        if question < int(value):
            res = False
            break
        else:
            question -= int(value)

if res:
    print("See you next month")
else:
    print("Adios")