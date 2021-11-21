t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())

    room = []

    for i in range(k+1):
        for j in range(n):
            if i == 0:
                room.append(j + 1)
            else:
                if j > 0:
                    room[j] += room[j-1]

    print(room[n-1])