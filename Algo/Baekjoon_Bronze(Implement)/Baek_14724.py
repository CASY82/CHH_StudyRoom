import sys

n = int(sys.stdin.readline())

dongari = "PROBRAIN,GROW,ARGOS,ADMIN,ANT,MOTION,SPG,COMON,ALMIGHTY".split(",")
hubo = [0 for _ in range(len(dongari))]

for i in range(len(dongari)):
    hubo[i] = max(list(map(int, sys.stdin.readline().split())))

print(dongari[hubo.index(max(hubo))])