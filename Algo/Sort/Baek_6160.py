import sys

n, k = map(int, sys.stdin.readline().split())

cowLevel = []
secondElection = []

for cnt in range(n):
    cowLevel.append((cnt + 1, list(map(int, sys.stdin.readline().split()))))

cowLevel.sort(key=lambda x : -x[1][0])

for i in range(k):
    secondElection.append(cowLevel[i])

secondElection.sort(key=lambda x : -x[1][1])

print(secondElection[0][0])
