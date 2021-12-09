import sys
n = int(sys.stdin.readline())

people = []

for _ in range(n):
    age, name = sys.stdin.readline().strip().split()
    age = int(age)
    people.append([age, name])

people.sort(key = lambda x : x[0])

for i,j in people:
    print(i, j)