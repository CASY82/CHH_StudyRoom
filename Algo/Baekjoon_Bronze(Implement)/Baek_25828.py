import sys

g, p, t = map(int, sys.stdin.readline().split())

total_people = g * p
group_people = t * p + g

if total_people < group_people:
    print(1)
elif total_people > group_people:
    print(2)
else:
    print(0)