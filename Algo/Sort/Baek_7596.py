import sys

cnt = 1
while True:
    play_list = int(sys.stdin.readline())
    music = []

    if play_list == 0:
        break

    for _ in range(play_list):
        music.append(sys.stdin.readline().strip())

    music.sort()

    print(cnt)
    for song in music:
        print(song)

    cnt += 1