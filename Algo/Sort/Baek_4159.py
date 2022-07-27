import sys

while True:
    n = int(sys.stdin.readline())

    location = []

    if n == 0:
        break

    for _ in range(n):
        location.append(int(sys.stdin.readline()))

    location.sort()

    now = 0
    result = True

    for i in location:
        if i - now <= 200:
            now = i
        else:
            result = False
            break

    #왕복 했을 때, 즉 도착 지점에는 전기 충전소가 없다는 가정... 이부분 간과함
    if 1422 - now > 100:
        result = False

    if result:
        print("POSSIBLE")
    else:
        print("IMPOSSIBLE")