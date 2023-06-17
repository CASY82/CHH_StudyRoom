import sys

m, n = map(int, sys.stdin.readline().split())

now = [0, 0]
dir_now = 0

#dir_list = ['e', 'n', 'w', 's']
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for _ in range(n):
    command = list(sys.stdin.readline().strip().split())

    if command[0] == 'TURN':
        if command[1] == '0':
            dir_now += 1
            if dir_now > 3:
                dir_now = 0
        else:
            dir_now -= 1
            if dir_now < -3:
                dir_now = 0
    elif command[0] == 'MOVE':
        now[0] += dx[dir_now] * int(command[1])
        now[1] += dy[dir_now] * int(command[1])

        if 0 <= now[0] <= m and 0 <= now[1] <= m:
            continue
        else:
            print(-1)
            exit()
print(*now)