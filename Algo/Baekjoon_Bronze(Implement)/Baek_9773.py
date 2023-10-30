import sys

n = int(sys.stdin.readline())

for _ in range(n):
    card_id = sys.stdin.readline().strip()
    sum_num = 0

    for i in range(len(card_id)):
        sum_num += int(card_id[i])

    tmp = (int(card_id) % 1000) * 10
    if tmp < 1000:
        tmp += 1000

    result = str(tmp + sum_num)
    print(result[-4:])