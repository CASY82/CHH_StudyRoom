import sys

bullshitword = ['he', 'she', 'her', 'him']

n = int(sys.stdin.readline())

sentence = list(sys.stdin.readline().strip().split())
result = 0

for i in range(n):
    for j in range(4):
        if bullshitword[j] == sentence[i]:
            result += 1

print(result)