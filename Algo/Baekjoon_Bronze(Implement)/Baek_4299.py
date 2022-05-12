import sys

sum_score, diff_score = map(int, sys.stdin.readline().split())

if((sum_score + diff_score) % 2 != 0 or (sum_score - diff_score) % 2 != 0 or sum_score < diff_score):
    print(-1)
else:
    print((sum_score + diff_score) // 2, abs(sum_score - diff_score) // 2)