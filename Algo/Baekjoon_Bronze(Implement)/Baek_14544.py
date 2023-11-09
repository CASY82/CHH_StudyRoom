import sys

t = int(sys.stdin.readline())

for i in range(t):
    n, m = map(int, sys.stdin.readline().split())

    candidate = dict()

    for _ in range(n):
        name = sys.stdin.readline().strip()

        candidate[name] = 0

    for _ in range(m):
        names, votes, local = sys.stdin.readline().strip().split()

        candidate[names] += int(votes)

    max_value = max(candidate.values())
    max_keys = [key for key, value in candidate.items() if value == max_value]

    if len(max_keys) > 1:
        print("VOTE {0}: THERE IS A DILEMMA".format(i + 1))
    else:
        print("VOTE {0}: THE WINNER IS {1} {2}".format(i + 1, max_keys[0], max_value))