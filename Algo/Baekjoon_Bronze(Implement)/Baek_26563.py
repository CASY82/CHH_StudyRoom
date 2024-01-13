import sys

t = int(sys.stdin.readline())

for _ in range(t):
    friends_correct = int(sys.stdin.readline())
    correct = list(sys.stdin.readline().strip())
    pick_answer = list(sys.stdin.readline().strip())
    total = 0
    same_cnt = 0
    diff_cnt = 0

    for i in range(len(correct)):
        if correct[i] == pick_answer[i]:
            same_cnt += 1
        else:
            diff_cnt += 1

    total += min(friends_correct, same_cnt)
    total += len(correct) - max(same_cnt, friends_correct)

    print(total)