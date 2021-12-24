import sys

n = int(sys.stdin.readline())
people = []

for _ in range(n):
    name, day, month, year = sys.stdin.readline().strip().split()
    people.append([name, int(day), int(month), int(year)])

people.sort(key = lambda x : (x[3], x[2], x[1]), reverse=True)

print(people[0][0])
print(people[-1][0])