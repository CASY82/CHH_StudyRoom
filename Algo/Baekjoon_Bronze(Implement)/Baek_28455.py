import sys

n = int(sys.stdin.readline())
union_attack = 0
level = 0

character = []

for _ in range(n):
    character.append(int(sys.stdin.readline()))

character.sort(reverse=True)

if n < 42:
    length = len(character)
else:
    length = 42

for i in range(length):
    lev = character[i]

    if lev >= 250:
        union_attack += 5
    elif lev >= 200:
        union_attack += 4
    elif lev >= 140:
        union_attack += 3
    elif lev >= 100:
        union_attack += 2
    elif lev >= 60:
        union_attack += 1

    level += lev

print(level, union_attack)