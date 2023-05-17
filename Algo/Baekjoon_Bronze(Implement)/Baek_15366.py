import sys

n = int(sys.stdin.readline())

jipang = list(map(int, sys.stdin.readline().split()))
box = list(map(int, sys.stdin.readline().split()))
result = True

jipang.sort()
box.sort()

for i in range(n):
    if jipang[i] > box[i]:
        result = False
        break

if result:
    print("DA")
else:
    print("NE")