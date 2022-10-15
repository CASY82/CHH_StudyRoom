import sys

n, m = map(int, sys.stdin.readline().split())
word = []
word_double = []
result_check = []


for _ in range(n):
    word.append(sys.stdin.readline().strip())

for _ in range(n):
    word_double.append(sys.stdin.readline().strip())

for i in range(n):
    tmp = ""
    for j in range(len(word[i])):
        tmp += word[i][j] + word[i][j]

    if word_double[i] == tmp:
        result_check.append(0)
    else:
        result_check.append(1)

if sum(result_check) == 0:
    print("Eyfa")
else:
    print("Not Eyfa")