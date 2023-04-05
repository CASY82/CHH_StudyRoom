import sys

n = int(sys.stdin.readline())
marathon = set()

for _ in range((2 * n) - 1):
    participant = sys.stdin.readline().strip()

    if participant not in marathon:
        marathon.add(participant)
    else:
        marathon.remove(participant)

for fail in marathon:
    print(fail)