import sys

cnt = 1

while True:
    t = int(sys.stdin.readline())

    if t == 0:
        break

    setting = set()

    for _ in range(t):
        setting.add(sys.stdin.readline().strip())

    print("Week {0} {1}".format(cnt, len(setting)))

    cnt += 1