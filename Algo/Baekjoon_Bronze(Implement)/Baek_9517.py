import sys

now_people = int(sys.stdin.readline())
n = int(sys.stdin.readline())
time_limit = 210
now_time = 0

for _ in range(n):
    time, correct = sys.stdin.readline().strip().split()

    now_time += int(time)

    if now_time >= time_limit:
        break

    if correct == "T":
        now_people += 1

        if now_people > 8:
            now_people = 1

print(now_people)