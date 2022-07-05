import sys

n = int(sys.stdin.readline())

for _ in range(n):
    people_id, strategy, it, tech = map(int, sys.stdin.readline().split())

    total = strategy + it + tech
    result = "PASS"

    if total < 55 or strategy < 35 * 0.3 or it < 25 * 0.3 or tech < 40 * 0.3:
        result = "FAIL"

    print(people_id, total, result)