#딕셔너리로 풀면 좀더 짧아 질수 있을거 같다.
import sys
score = []
result = []

for _ in range(8):
    score.append(int(sys.stdin.readline()))

tmp = sorted(score)[3:8]
for i in tmp:
    result.append(score.index(i)+1)

result.sort()

print(sum(tmp))
for i in result:
    print(i, end=' ')