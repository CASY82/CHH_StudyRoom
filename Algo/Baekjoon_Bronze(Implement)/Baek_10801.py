a = list(map(int, input().split()))
b = list(map(int, input().split()))

aCounter = 0
bCounter = 0

for i in range(len(a)):
    if a[i] > b[i]:
        aCounter += 1
    elif a[i] < b[i]:
        bCounter += 1
    else:
        continue

if aCounter > bCounter:
    print('A')
elif aCounter < bCounter:
    print('B')
else:
    print('D')