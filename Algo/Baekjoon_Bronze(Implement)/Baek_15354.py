import sys

n = int(sys.stdin.readline())

next_check = ""
result = 0

for _ in range(n):
    person = sys.stdin.readline().strip()

    if next_check == "":
        next_check = person
        result += 1
    else:
        if next_check == person:
            continue
        else:
            result += 1
            next_check = person

print(result + 1)