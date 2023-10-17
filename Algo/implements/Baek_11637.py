import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n = int(sys.stdin.readline())

    votes = []

    for _ in range(n):
        votes.append(int(sys.stdin.readline()))

    result = votes.index(max(votes))

    if votes.count(max(votes)) > 1:
        print("no winner")
    else:
        total = sum(votes)

        if max(votes) > total / 2:
            print("majority winner {}".format(result + 1))
        else:
            print("minority winner {}".format(result + 1))