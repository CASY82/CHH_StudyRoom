import sys

n = int(sys.stdin.readline())
vote = list(map(int, sys.stdin.readline().split()))

score = [0 for _ in range(n + 1)]

for i in range(n):
    score[vote[i]] += 1

max_vote = max(score)
tmp_score = score[1:]

if tmp_score.count(max_vote) > 1:
    print("skipped")
else:
    try:
        tmp = tmp_score.index(max_vote) + 1

        print(tmp)
    except:
        print("skipped")