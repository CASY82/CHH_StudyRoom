t = int(input())

for _ in range(t):
    h, w, n = map(int, input().split())

    if n % h != 0:
        room_num = str((n // h) + 1).zfill(2)
        floor = n % h
    else:
        room_num = str(n // h).zfill(2)
        floor = h

    print(floor, room_num, sep='')

#반례
# 1
# 2 15 8
# 1
# 1 1 1