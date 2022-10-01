import sys

t = int(sys.stdin.readline())

for i in range(t):
    print("Scenario #{}:".format(i+1))
    word_cnt = int(sys.stdin.readline())

    word = []

    for _ in range(word_cnt):
        word.append(sys.stdin.readline().strip())

    user_cnt = int(sys.stdin.readline())
    users = []

    for _ in range(user_cnt):
        users.append(list(map(int, sys.stdin.readline().split())))

    result = []

    for user in range(len(users)):
        tmp = ""
        for pw in range(1, users[user][0] + 1):
            tmp += word[users[user][pw]]

        result.append(tmp)

    for res in result:
        print(res)

    print()