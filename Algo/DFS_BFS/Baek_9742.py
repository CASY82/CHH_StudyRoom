import sys

def backtrack(v, word, target):
    if v == len(word):
        cnt[0] += 1
        if cnt[0] == target:
            result.append(''.join(location))
            return

    else:
        if cnt[0] == target:
            return

        for i in range(len(word)):
            if visited[i]:
                visited[i] = False
                location.append(word[i])
                backtrack(v + 1, word, target)
                visited[i] = True
                location.pop()

while True:
    try:
        word, number = sys.stdin.readline().split()
    except:
        break

    number = int(number)
    location = []
    visited = [True for _ in range(len(word))]
    cnt = [0]
    result = []

    backtrack(0, word, number)

    if result:
        print(word, number, "=", result[0])
    else:
        print(word, number, "=", "No permutation")