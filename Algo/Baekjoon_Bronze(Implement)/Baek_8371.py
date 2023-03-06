import sys

n = int(sys.stdin.readline())

first_word = sys.stdin.readline().strip()
compare_word = sys.stdin.readline().strip()

cnt = 0

for i in range(n):
    if first_word[i] != compare_word[i]:
        cnt += 1

print(cnt)