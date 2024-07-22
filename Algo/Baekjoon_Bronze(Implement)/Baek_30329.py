import sys

kick_string = sys.stdin.readline().strip()

count = 0
start = 0

while True:
    start = kick_string.find("kick", start)

    if start == -1:
        break

    count += 1
    start += 1

print(count)