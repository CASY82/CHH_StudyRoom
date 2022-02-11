count = 0

for _ in range(6):
    result = input()

    if result == 'W':
        count += 1

if count >= 5:
    print(1)
elif count >= 3:
    print(2)
elif count >= 1:
    print(3)
else:
    print(-1)