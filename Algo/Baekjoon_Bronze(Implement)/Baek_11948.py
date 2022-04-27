import sys

fir_score = []
sec_score = []

for _ in range(4):
    fir_score.append(int(sys.stdin.readline().strip()))

for _ in range(2):
    sec_score.append(int(sys.stdin.readline().strip()))

fir_score.sort(reverse=True)
sec_score.sort(reverse=True)

result = sum(fir_score) - fir_score[-1] + sec_score[0]

print(result)
