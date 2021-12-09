import sys

n = int(sys.stdin.readline())
cnt = 0
start = 666

while cnt < n:
    start_str = str(start)

    if '666' in start_str:
        cnt += 1

    result = start
    start += 1

print(result)