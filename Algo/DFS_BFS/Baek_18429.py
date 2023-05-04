import sys

n, k = map(int, sys.stdin.readline().split())
exercise_kit = list(map(int, sys.stdin.readline().split()))

can_cnt = [0]
now_weight = [500]
exercise_list = []
check = [True] * n

def backtrack(x):
    if x == n:
        can_cnt[0] += 1

    else:
        for i in range(len(exercise_kit)):
            if check[i]:
                if now_weight[0] + exercise_kit[i] - k >= 500:
                    now_weight[0] += exercise_kit[i] - k
                    check[i] = False
                    backtrack(x + 1)
                    check[i] = True
                    now_weight[0] -= exercise_kit[i] - k
backtrack(1)
print(can_cnt[0])