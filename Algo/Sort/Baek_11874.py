import sys

n, m, k = map(int, sys.stdin.readline().split())

subject = dict()
check = []

for _ in range(n):
    title, score = sys.stdin.readline().strip().split()

    score = int(score)

    subject[title] = score

open_score = 0

for _ in range(k):
    sub = sys.stdin.readline().strip()
    open_score += subject[sub]

    del subject[sub]

scores = sorted(subject.values())

min_score = open_score
max_score = open_score

for i in range(m - k):
    min_score += scores[i]
    max_score += scores[-i - 1]

print(min_score, max_score)

# 다른 사람 풀이
# def main():
#     N, M, K = tuple(map(int, input().strip().split(' ')))
#     scores = dict()
#     for n in range(N):
#         course, grade = input().strip().split(' ')
#         grade = int(grade)
#         scores[course] = grade
#     score_sum_K = 0
#     for k in range(K):
#         course = input().strip()
#         score_sum_K += scores[course]
#         del scores[course]
#     score_unincluded_sorted = sorted(scores.values())
#     print(
#         score_sum_K + sum(score_unincluded_sorted[:M-K]),
#         score_sum_K + sum(score_unincluded_sorted[N-M:]),
#     )
#
# if __name__ == '__main__':
#     main()