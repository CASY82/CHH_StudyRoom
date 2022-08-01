import sys

n = sys.stdin.readline().strip()

length = len(n)

right = 0
left = 0

for i in range((length // 2)):
    left += int(n[i])

for j in range((length // 2), length):
    right += int(n[j])

if right == left:
    print("LUCKY")
else:
    print("READY")