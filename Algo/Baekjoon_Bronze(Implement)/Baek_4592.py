import sys

while True:
    check = sys.stdin.readline().strip().split()

    if check[0] == '0':
        break

    tmp = ''
    for i in range(1, len(check)):
        if check[i] != tmp:
            tmp = check[i]
            print(check[i], end=" ")

    print("$")