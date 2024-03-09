import sys

fox_sign = [(1, 4), (1, 3), (3, 4)]
exist = [0, 0, 0]

n = int(sys.stdin.readline())
result = True

for _ in range(n):
    finger = list(map(int, sys.stdin.readline().split()))
    finger.sort()

    if (finger[0], finger[1]) in fox_sign:
        for i in range(3):
            if fox_sign[i] == (finger[0], finger[1]):
                exist[i] += 1
    else:
        result = False
        break

if result:
    for j in range(3):
        if exist[j] == 0:
            print("Woof-meow-tweet-squeek")
            exit()

    print("Wa-pa-pa-pa-pa-pa-pow!")
else:
    print("Woof-meow-tweet-squeek")

# 다른 사람 풀이
# s = []
# for _ in range(int(input())):
#     c = input()
#     t = int(c[0]+c[2] if c[0]<c[2] else c[2]+c[0])
#     s += t,
# s.sort()
# print('Wa-pa-pa-pa-pa-pa-pow!' if s==[13,14,34] else 'Woof-meow-tweet-squeek')