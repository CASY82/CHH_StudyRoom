import sys
from collections import deque

t = int(sys.stdin.readline())

for _ in range(t):
    situation = list(sys.stdin.readline().strip())
    n = int(sys.stdin.readline())
    num_array = sys.stdin.readline().strip().split(",")
    num_array[0] = num_array[0].replace("[", "")
    num_array[-1] = num_array[-1].replace("]", "")

    if num_array[0] == "":
        num_array.pop()

    try:
        tmp = deque(num_array)
        cnt = 0

        for i in range(len(situation)):
            if situation[i] == 'R':
                cnt += 1
            else:
                if cnt % 2 == 1:
                    tmp.pop()
                else:
                    tmp.popleft()

    except:
        print("error")
        continue

    print("[", sep="", end="")
    if cnt % 2 == 0:
        for j in range(len(tmp)):
            if j == len(tmp)-1:
                print(tmp[j], end="")
            else:
                print(tmp[j], ",", sep="", end="")
    else:
        for j in range(len(tmp)-1, -1, -1):
            if j == 0:
                print(tmp[j], end="")
            else:
                print(tmp[j], ",", sep="", end="")

    print("]", sep="")