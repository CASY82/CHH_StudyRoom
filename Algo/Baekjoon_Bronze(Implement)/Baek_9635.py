import sys

t = int(sys.stdin.readline())

for _ in range(t):
    n, x, y = map(int, sys.stdin.readline().split())
    nums = list(map(int, sys.stdin.readline().split()))

    easy_chk = True
    hard_chk = True

    if nums[0] == x:
        easy_chk = False

    if nums[-1] == y:
        hard_chk = False

    if easy_chk and hard_chk:
        print("OKAY")
    elif not easy_chk and hard_chk:
        print("EASY")
    elif not hard_chk and easy_chk:
        print("HARD")
    else:
        print("BOTH")