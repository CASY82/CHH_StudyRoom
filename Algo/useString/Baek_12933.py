import sys

duck = sys.stdin.readline().strip()

visited = [0 for i in range(len(duck))]

quack = ["q", "u", "a", "c", "k"]
cnt = 0
check = True

if len(duck) % 5 == 0:
    while True:
        j = 0
        tmp = visited[:]
        incheck = True
        for i in range(len(duck)):
            if j == len(quack):
                incheck = False
                j = 0
            if visited[i] == 0:
                if duck[i] == quack[j]:
                    visited[i] = 1
                    j += 1

        if j == len(quack):
            incheck = False

        cnt += 1

        if tmp == visited or incheck:
            check = False
            break

        if visited.count(0) == 0:
            break

    if check:
        print(cnt)
    else:
        print(-1)
else:
    print(-1)