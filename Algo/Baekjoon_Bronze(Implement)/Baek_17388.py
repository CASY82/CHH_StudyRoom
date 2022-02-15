import sys

university = ["Soongsil", "Korea", "Hanyang"]
score = list(map(int, sys.stdin.readline().split()))

if sum(score) >= 100:
    print("OK")
else:
    print(university[score.index(min(score))])