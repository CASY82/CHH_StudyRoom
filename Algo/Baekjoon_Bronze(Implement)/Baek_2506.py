n = int(input())
grading = list(map(int, input().split()))
check = False
total = 0
score = 1

for i in range(n):
    if grading[i] == 1:
        total += score
        score += 1
    else:
        score = 1

print(total)