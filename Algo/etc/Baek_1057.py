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

#음... 나 왜이렇게 어렵게 풀었지? 지금보니 player 배열이 전혀 필요가 없다.
# N, k, l = map(int,input().split())
# cnt = 0
# while k != l:
#     cnt += 1
#     k -= k // 2
#     l -= l // 2
# print(cnt)