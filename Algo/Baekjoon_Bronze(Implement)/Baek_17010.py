l = int(input())

for _ in range(l):
    num, character = input().split()

    num = int(num)

    for i in range(num):
        print(character, end='')

    print()