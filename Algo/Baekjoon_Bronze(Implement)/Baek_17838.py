import sys

t = int(sys.stdin.readline())

for _ in range(t):
    command = sys.stdin.readline().strip()

    pattern = "1122122"
    command_pattern = ""

    if len(command) == 7:
        key1 = command[0]
        key2 = command[2]

        for i in range(len(command)):
            if command[i] == key1:
                command_pattern += "1"
            else:
                command_pattern += "2"

    if command_pattern == pattern:
        print(1)
    else:
        print(0)