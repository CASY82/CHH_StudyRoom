people, jimin, hansu = map(int, input().split())
player = [i for i in range(1, people + 1)]
count = 1

while True:
    if ((jimin + 1) // 2) == ((hansu + 1) // 2):
        break

    for i in range(len(player)):
        player[i] = (player[i] + 1) // 2

    player = list(set(player))
    jimin = ((jimin + 1) // 2)
    hansu = ((hansu + 1) // 2)

    count += 1
    if len(player) <= 2:
        break

print(count)