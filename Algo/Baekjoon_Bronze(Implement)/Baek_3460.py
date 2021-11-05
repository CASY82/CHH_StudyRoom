t = int(input())

for _ in range(t):
    n = int(input())

    check = list(format(n, 'b'))
    check.reverse()
    for i in range(len(check)):
        if check[i] == '1':
            print(i, end=' ')