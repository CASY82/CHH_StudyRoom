import sys

lottery = []

for _ in range(6):
    number, money = sys.stdin.readline().strip().split()
    lottery.append((number, int(money)))

while True:
    lottery_num = sys.stdin.readline().strip()
    result = 0

    if lottery_num == '-1':
        break

    for i in range(6):
        if i == 0:
            if lottery[i][0] == lottery_num:
                result += lottery[i][1]
        elif 1 <= i <= 2:
            if lottery[i][0] == lottery_num[:3]:
                result += lottery[i][1]
        elif 3 <= i <= 4:
            if lottery[i][0] == lottery_num[3:]:
                result += lottery[i][1]
        elif i == 5:
            if lottery[i][0] == lottery_num[4:]:
                result += lottery[i][1]

    print(result)