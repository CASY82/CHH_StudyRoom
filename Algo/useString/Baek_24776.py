import sys

candidate = dict()
max_votes = 0

while True:
    name = sys.stdin.readline().strip()

    if name == "***":
        break

    if name not in candidate:
        candidate[name] = 1
    else:
        candidate[name] += 1

    if candidate[name] > max_votes:
        max_votes = candidate[name]

max_keys = [k for k, v in candidate.items() if v == max_votes]

if len(max_keys) > 1:
    print("Runoff!")
else:
    print(max_keys[0])