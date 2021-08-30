count = 0

while True:
    o, w = map(int, input().split())

    if o == 0 and w == 0:
        break

    while True:
        effect, num = map(str, input().split())

        if effect == '#' and num == '0':
            count += 1
            break

        if w > 0:
            if effect == 'F':
                w += int(num)
            else:
                w -= int(num)
        else:
            continue

    if w > (o * 0.5) and w < (o * 2):
        print(count, ':-)')
    elif w <= 0:
        print(count, 'RIP')
    else:
        print(count, ':-(')