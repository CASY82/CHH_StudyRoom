import sys

n = int(sys.stdin.readline())

gong_yak = ["Never gonna give you up", "Never gonna let you down", "Never gonna run around and desert you", "Never gonna make you cry", "Never gonna say goodbye", "Never gonna tell a lie and hurt you", "Never gonna stop"]
check = False

for _ in range(n):
    sentence = sys.stdin.readline().strip()

    if sentence not in gong_yak:
        check = True

if check:
    print("Yes")
else:
    print("No")