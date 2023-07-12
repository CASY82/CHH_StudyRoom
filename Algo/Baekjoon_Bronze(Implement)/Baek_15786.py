import sys

n, m = map(int, sys.stdin.readline().split())

origin_word = sys.stdin.readline().strip()

for _ in range(m):
    postit = sys.stdin.readline().strip()
    pointer = 0
    result = False

    for i in range(len(postit)):
        if origin_word[pointer] == postit[i]:
            pointer += 1

        if pointer >= n:
            result = True
            break

    if result:
        print('true')
    else:
        print('false')