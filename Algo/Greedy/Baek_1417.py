import sys

n = int(sys.stdin.readline())
vote = []
cnt = 0

for _ in range(n):
    vote.append(int(sys.stdin.readline()))

if n > 1:
    tmp_vote = vote[1:]
    while max(tmp_vote) >= vote[0]:
        if max(tmp_vote) >= vote[0]:
            tmp_vote[tmp_vote.index(max(tmp_vote))] -= 1
            vote[0] += 1
            cnt += 1

print(cnt)