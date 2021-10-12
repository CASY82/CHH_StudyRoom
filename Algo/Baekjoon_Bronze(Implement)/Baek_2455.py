train = 0
max_people = 0

for _ in range(4):
    outer, inner = map(int, input().split())

    train += inner
    train -= outer

    if max_people < train:
        max_people = train

print(max_people)