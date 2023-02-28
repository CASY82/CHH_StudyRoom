import sys

k = int(sys.stdin.readline())

tmp = list(format(k, 'b'))

cnt = 0
for i in range(len(tmp)):
    if tmp[i] == '1':
        cnt = i

if cnt == 0:
    if k == 1:
        print(1, 1)
    else:
        print(k, 0)
else:
    print(2 ** len(tmp), cnt + 1)