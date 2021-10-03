n = int(input())
counter = 0
l_n = 6
l = 6
diff = 3

if n <= 4:
    print(4)
else:
    while n > l_n:

        l_n += diff
        l += 2

        if counter % 2 == 1:
            diff += 1
            counter = 0
        else:
            counter += 1

    print(l)