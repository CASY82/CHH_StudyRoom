train = 0
max_value = 0

for i in range(10):
    outer, inner = map(int, input().split())

    train += inner
    train -= outer

    if max_value < train:
        max_value = train

print(max_value)