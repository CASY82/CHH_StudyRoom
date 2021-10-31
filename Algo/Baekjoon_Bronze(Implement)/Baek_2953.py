result = []

for _ in range(5):
    score = list(map(int, input().split()))

    result.append(sum(score))

print(result.index(max(result)) + 1, max(result))