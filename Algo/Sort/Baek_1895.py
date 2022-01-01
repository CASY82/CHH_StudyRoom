import sys

r, c = map(int, sys.stdin.readline().split())
image = []

for _ in range(r):
    image.append(list(map(int, sys.stdin.readline().split())))

t = int(sys.stdin.readline())

cnt = 0

#필터
def filter(x, y):
    tmp = []
    for i in range(y, y+3):
        for j in range(x, x+3):
            tmp.append(image[i][j])

    tmp.sort()

    return tmp[4]

for a in range(r-2):
    for b in range(c-2):
        check = filter(b,a)
        if check >= t:
            cnt += 1

print(cnt)