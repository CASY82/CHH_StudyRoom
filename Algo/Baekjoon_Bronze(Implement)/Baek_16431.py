bessie = list(map(int, input().split()))
daisy = list(map(int, input().split()))
john = list(map(int, input().split()))

bessieDistance = int(((bessie[0] - john[0]) ** 2 + (bessie[1] - john[1]) ** 2) ** 0.5)
daisyDistance = int(abs(daisy[0] - john[0])) + int(abs(daisy[1] - john[1]))

if bessieDistance < daisyDistance:
    print("bessie")
elif bessieDistance > daisyDistance:
    print("daisy")
else:
    print("tie")