import sys

score = dict()
correct = []
result = 0

while True:
    logs = list(sys.stdin.readline().strip().split())

    if logs[0] == '-1':
        break

    if logs[1] not in score:
        score[logs[1]] = 1
    else:
        score[logs[1]] += 1

    if logs[2] == "right":
        correct.append(logs[1])
        result += int(logs[0])

for question in correct:
    result += (score[question] - 1) * 20

print(len(correct), result)