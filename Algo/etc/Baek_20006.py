import sys

p, m = map(int, sys.stdin.readline().split())

room = dict()
room_num = 0

for _ in range(p):
    level, nickname = sys.stdin.readline().strip().split()
    level = int(level)

    if room_num == 0:
        room_num += 1
        room[room_num] = [(level, nickname)]
    else:
        no_create = True
        for key in room:
            if len(room[key]) < m:
                if room[key][0][0] - 10 <= level <= room[key][0][0] + 10:
                    room[key].append((level, nickname))
                    no_create = False
                    break

        if no_create:
            room_num += 1
            room[room_num] = [(level, nickname)]

for key, val in room.items():
    if len(val) == m:
        print("Started!")
    else:
        print("Waiting!")
    val.sort(key=lambda x:x[1])
    for lv, name in val:
        print(lv, name)