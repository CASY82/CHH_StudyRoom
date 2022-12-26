import sys

t = int(sys.stdin.readline())

for _ in range(t):
    num = sys.stdin.readline().strip()
    result = ""

    tmp = num[0]
    cnt = 1
    for i in range(1, len(num)):
        if tmp == num[i]:
            cnt += 1
        else:
            result += str(cnt) + tmp
            cnt = 1
            tmp = num[i]

    result += str(cnt) + tmp

    print(result)