import sys

n = int(sys.stdin.readline())
tmp = []

for _ in range(n):
    name, ram, cpu, drive = sys.stdin.readline().strip().split()

    ram = int(ram)
    cpu = int(cpu)
    drive = int(drive)

    favorite = 2 * ram + 3 * cpu + drive
    tmp.append([name, favorite])

tmp.sort(key=lambda x:x[0], reverse=True)
tmp.sort(key=lambda x:x[1])

if n > 0:
    print(tmp[-1][0])
if n > 1:
    print(tmp[-2][0])