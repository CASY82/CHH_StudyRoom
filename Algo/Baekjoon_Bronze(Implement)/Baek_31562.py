import sys

n, m = map(int, sys.stdin.readline().split())
song = dict()

for _ in range(n):
    num, name, *music = sys.stdin.readline().strip().split()

    song[name] = "".join(music)

for _ in range(m):
    test = "".join(sys.stdin.readline().strip().split())

    cnt = 0
    res = []

    for key, val in song.items():
        if test in val[:3]:
            cnt += 1
            res.append(key)

    if cnt == 1:
        print(res[0])
    elif cnt > 1:
        print("?")
    elif cnt == 0:
        print("!")