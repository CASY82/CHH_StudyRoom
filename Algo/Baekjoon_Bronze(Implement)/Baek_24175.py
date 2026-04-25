# Tokyo2020

import sys
from collections import defaultdict

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    total = defaultdict(list)

    for _ in range(n):
        y, s, m = sys.stdin.readline().split()

        y = int(y)

        total[y].append(m)

    max_gold = -1
    max_total = -1
    gold_year = 0
    total_year = 0

    for year, medals in total.items():
        gold_count = medals.count("Gold")
        total_count = len(medals)

        if gold_count > max_gold:
            max_gold = gold_count
            gold_year = year
        elif gold_count == max_gold and year < gold_year:
            gold_year = year

        if total_count > max_total:
            max_total = total_count
            total_year = year
        elif total_count == max_total and year < total_year:
            total_year = year

    print(gold_year, total_year)