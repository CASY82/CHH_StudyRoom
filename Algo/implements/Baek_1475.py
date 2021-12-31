import sys

roomNum = sys.stdin.readline().strip()
numCount = [0 for i in range(10)]

for i in range(len(roomNum)):
    if (int(roomNum[i]) == 6 or int(roomNum[i]) == 9):
        if numCount[6] > numCount[9]:
            numCount[9] += 1
        elif numCount[6] <= numCount[9]:
            numCount[6] += 1
    else:
        numCount[int(roomNum[i])] += 1

print(max(numCount))