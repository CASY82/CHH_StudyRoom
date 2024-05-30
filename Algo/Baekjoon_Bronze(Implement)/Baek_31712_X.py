# 왜이렇게 어렵게 생각한거야;;

damages = [list(map(int, input().split())) for _ in range(3)]
hp = int(input())
time = -1

while hp > 0:
    time += 1

    for damage in damages:
        if time % damage[0] == 0:
            hp -= damage[1]

print(time)