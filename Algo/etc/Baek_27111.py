import sys

n = int(sys.stdin.readline())
person_list = set()
error_cnt = 0

for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    if a not in person_list and b == 1:
        person_list.add(a)
    elif a not in person_list and b == 0:
        error_cnt += 1
    elif a in person_list and b == 1:
        error_cnt += 1
    elif a in person_list and b == 0:
        person_list.remove(a)

res = error_cnt + len(person_list)

print(res)