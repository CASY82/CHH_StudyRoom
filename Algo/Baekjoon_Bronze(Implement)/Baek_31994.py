import sys

semina = []

for i in range(7):
    name, person = sys.stdin.readline().strip().split()
    semina.append((name, int(person)))

semina.sort(key=lambda x:x[1])

print(semina[-1][0])