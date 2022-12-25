import sys

n = int(sys.stdin.readline())
crane = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
container = list(map(int, sys.stdin.readline().split()))

crane.sort(reverse=True)
container.sort(reverse=True)

time = 0

# 아.. 조건 하나 까먹어서 틀림
if crane[0] < container[0]:
    print(-1)
else:
    while container:
        if not container:
            break

        # 이렇게하면 시간 초과 날거같았는데 pypy는 통과하는게 신기하네;;
        for c in crane:
            for b in container:
                if c >= b:
                    container.remove(b)
                    break

        time += 1

    print(time)

# remove 함수를 사용하여 시간복잡도가 높아지는데, 그걸 방지하여 해결한 참고 코드
# import sys
#
# input = sys.stdin.readline
#
# n = int(input())
# crane = list(map(int, input().split()))
# m = int(input())
# box = list(map(int, input().split()))
#
# crane.sort(reverse=True)
# box.sort(reverse=True)
#
#
# box_moved = [0] * m
# crane_next = [0] * n
#
# move_count = 0
# time = 0
#
# if box[0] > crane[0]:
#     print(-1)
# else:
#     while move_count < m:
#         for i in range(n):
#             while crane_next[i] < m:
#                 if not box_moved[crane_next[i]] and crane[i] >= box[crane_next[i]]:
#                     box_moved[crane_next[i]] = 1
#                     crane_next[i] += 1
#                     move_count += 1
#                     break
#
#                 crane_next[i] += 1
#
#         time += 1
#
#     print(time)