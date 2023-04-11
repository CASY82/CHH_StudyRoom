import sys

sequence = sys.stdin.readline().strip()

ball = [1, 0, 0, 2]

for method in range(len(sequence)):
    if sequence[method] == 'A':
        ball[0], ball[1] = ball[1], ball[0]
    elif sequence[method] == 'B':
        ball[0], ball[2] = ball[2], ball[0]
    elif sequence[method] == 'C':
        ball[0], ball[3] = ball[3], ball[0]
    elif sequence[method] == 'D':
        ball[1], ball[2] = ball[2], ball[1]
    elif sequence[method] == 'E':
        ball[1], ball[3] = ball[3], ball[1]
    elif sequence[method] == 'F':
        ball[2], ball[3] = ball[3], ball[2]

print(ball.index(1) + 1)
print(ball.index(2) + 1)