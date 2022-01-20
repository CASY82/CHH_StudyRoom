import sys

n = int(sys.stdin.readline())
remainPeople = dict()

for _ in range(n):
    person, state = sys.stdin.readline().strip().split()

    if state == "enter":
        remainPeople[person] = 1
    else:
        del(remainPeople[person])

for i in sorted(remainPeople.keys(), reverse= True):
    print(i)