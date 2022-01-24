import sys

result = ''
cnt = 0

while True:
    command = sys.stdin.readline().strip()

    if command == '=':
        break

    if command == '/':
        command = '//'

    result += command
    cnt += 1

    if cnt == 3:
        result = str(eval(result))
        cnt = 1

print(eval(result))