import sys

n = int(sys.stdin.readline())
max_cnt = 0

for _ in range(n):
    loop_word = sys.stdin.readline().strip()

    tmp = 0
    tmp += loop_word.count("for")
    tmp += loop_word.count("while")

    max_cnt = max(max_cnt, tmp)

print(max_cnt)