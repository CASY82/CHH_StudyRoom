t = int(input())

for _ in range(t):
    mis, word = input().split()

    mis = int(mis)

    print(word[:mis-1], word[mis:], sep='')
