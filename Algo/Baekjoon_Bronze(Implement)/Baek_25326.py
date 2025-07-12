import sys
from collections import Counter

n, m = map(int, sys.stdin.readline().split())

# 1) 학생 데이터 읽어서 카운팅
counts = Counter()
for _ in range(n):
    subj, fruit, color = sys.stdin.readline().strip().split()
    counts[(subj, fruit, color)] += 1

# 2) 질의 처리
# 가능한 값들 정의
S = ['kor', 'eng', 'math']
F = ['apple', 'pear', 'orange']
C = ['red', 'blue', 'green']

for i in range(1, m+1):
    qs, qf, qc = sys.stdin.readline().strip().split()
    # '-' 이면 전체 리스트, 아니면 그 조건값만
    subs = S if qs == '-' else [qs]
    fruits = F if qf == '-' else [qf]
    colors = C if qc == '-' else [qc]

    ans = 0
    # 3중 루프: 최대 27회
    for s in subs:
        for f in fruits:
            for c in colors:
                ans += counts[(s, f, c)]

    print(ans)
