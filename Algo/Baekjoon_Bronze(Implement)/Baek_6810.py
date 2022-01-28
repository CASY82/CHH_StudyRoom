result = (9 * 1 + 7 * 3 + 8 * 1 + 0 * 3 + 9 * 1 + 2 * 3 + 1 * 1 + 4 * 3 + 1 * 1 + 8 * 3)

for i in range(3):
    num = int(input())

    if i % 2 == 0:
        result += num * 1
    else:
        result += num * 3

print("The 1-3-sum is", result)