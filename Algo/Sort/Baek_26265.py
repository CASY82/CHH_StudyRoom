import sys

from operator import itemgetter

input = sys.stdin.readline
n = int(input())
pairs = [input().split() for _ in range(n)]

# 1) 멘티 내림차순
pairs.sort(key=itemgetter(1), reverse=True)
# 2) 멘토 오름차순 (안정 정렬이라 1)의 결과가 멘토 그룹 내에서 유지됨)
pairs.sort(key=itemgetter(0))

print('\n'.join(f'{a} {b}' for a, b in pairs))