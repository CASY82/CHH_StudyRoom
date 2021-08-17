x, y, w, h = map(int, input().split())

right = w - x
left = x - 0
up = h - y
down = y - 0

print(min(right, left, up, down))