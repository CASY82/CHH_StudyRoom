while True:
    try:
        x1, y1, x2, y2, x3, y3, x4, y4 = map(float, input().split())
    except:
        break

    if x1 == x3 and y1 == y3:
        x = x2 + x4 - x1
        y = y2 + y4 - y1

    if x1 == x4 and y1 == y4:
        x = x2 + x3 - x1
        y = y2 + y3 - y1

    if x2 == x3 and y2 == y3:
        x = x4 + x1 - x2
        y = y4 + y1 - y2

    if x2 == x4 and y2 == y4:
        x = x1 + x3 - x2
        y = y1 + y3 - y2

    print("{:.3f}".format(x), "{:.3f}".format(y))
