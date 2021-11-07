num = list(map(int, input().split()))
sequence = list(input())

num.sort()

for i in range(3):
    if sequence[i] == 'A':
        print(num[0], end=' ')
    elif sequence[i] == 'B':
        print(num[1], end=' ')
    else:
        print(num[2], end=' ')