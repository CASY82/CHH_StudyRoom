import sys

t = int(sys.stdin.readline())
result = []

for _ in range(t):
    word = sys.stdin.readline().strip()

    alpha_set = set()

    for alpha in range(len(word)):
        if word[alpha] not in alpha_set:
            alpha_set.add(word[alpha])

    result.append(len(alpha_set))

print(max(result))