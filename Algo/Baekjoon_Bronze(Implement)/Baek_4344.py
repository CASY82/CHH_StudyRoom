t = int(input())

for _ in range(t):
    score = list(map(int, input().split()))
    average = 0
    count = 0
    sum = 0

    for i in range(1, len(score)):
        sum += score[i]

    average = sum // score[0]

    for j in range(1, len(score)):
        if score[j] > average:
            count += 1

    result = count * 100 / score[0]

    print(str("{:0,.3f}".format(result)) + '%')