import sys

n = int(sys.stdin.readline())
gahui_pick = int(sys.stdin.readline())
votes = list(map(int, sys.stdin.readline().split()))

votes.sort(reverse=True)

for i in range(n - 1):
    if gahui_pick > votes[i]:
        print(i + 1)
        exit()

print(n)