t = int(input())

for _ in range(t):
    quiz = input()
    result = 0
    count = 0

    for i in range(len(quiz)):
        if quiz[i] == 'O':
            count += 1
            result += count
        else:
            count = 0

    print(result)