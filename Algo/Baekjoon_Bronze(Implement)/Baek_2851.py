mush = []
result = 0

for _ in range(10):
    mush.append(int(input()))

for i in range(len(mush)):
    result += mush[i]

    if result >= 100:
        if result == 100:
            break
        else:
            if abs(100 - (result - mush[i])) >= abs(100 - result):
                break
            else:
                result -= mush[i]
                break

print(result)