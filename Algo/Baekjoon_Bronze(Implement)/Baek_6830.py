import sys

tmp = []
while True:
    city, degree = sys.stdin.readline().strip().split()

    tmp.append([int(degree), city])

    if city == "Waterloo":
        break

tmp.sort(key= lambda x:x[0])
print(tmp[0][1])