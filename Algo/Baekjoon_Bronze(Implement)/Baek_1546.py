n = int(input())
subject = list(map(int, input().split()))

score = []

for i in subject:
    score.append((i / max(subject)) * 100)

average = sum(score) / len(score)

print(average)