n = int(input())
side = [0 for i in range(4)]
axis = 0

for _ in range(n):
    x, y = map(int, input().split())

    if x != 0 and y != 0:
        if x > 0 and y > 0:
            side[0] += 1
        elif x < 0 and y > 0:
            side[1] += 1
        elif x < 0 and y < 0:
            side[2] += 1
        else:
            side[3] += 1
    else:
        axis += 1

for i in range(4):
    print("Q", (i+1), ": ", side[i], sep='')

print("AXIS:", axis)