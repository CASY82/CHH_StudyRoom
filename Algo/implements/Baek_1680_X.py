import sys

t = int(sys.stdin.readline())

for _ in range(t):
    w, n = map(int, sys.stdin.readline().split())

    now_weight = 0
    result = 0
    pre_distance = 0

    for i in range(n):
        x_i, w_i = map(int, sys.stdin.readline().split())

        if now_weight + w_i < w:
            result += x_i - pre_distance
            now_weight += w_i
        elif now_weight + w_i == w:
            result += (x_i - pre_distance) + x_i * 2
            now_weight = 0
            if i == n - 1:
                result -= x_i * 2
        elif now_weight + w_i > w:
            now_weight = w_i
            result += (x_i - pre_distance) + x_i * 2
        pre_distance = x_i

    if i == n-1:
        result += x_i

    print(result)

# if __name__ == '__main__':
#     for _ in range(int(input())):
#         w, n = map(int, input().split())
#         testcase = []
#         for __ in range(n):
#             x_i, w_i = map(int, input().split())
#             testcase.append([x_i, w_i])
#
#         capacity = 0
#         distance = 0
#         previous_value = 0
#         for i in testcase:
#             # i[0]: 쓰레기장으로부터의 거리   i[1]: 쓰레기의 양
#             if capacity + i[1] < w:
#                 distance += i[0] - previous_value
#                 capacity += i[1]
#             elif capacity + i[1] == w:
#                 distance += (i[0] - previous_value) + i[0] * 2
#                 capacity = 0
#                 if testcase.index(i) == n - 1:
#                     distance -= i[0] * 2
#             elif capacity + i[1] > w:
#                 capacity = i[1]
#                 distance += (i[0] - previous_value) + i[0] * 2
#             previous_value = i[0]
#
#         # 모든 쓰레기를 수거하여 다시 쓰레기장으로 돌아갈 때
#         if testcase.index(i) == n - 1:
#             distance += i[0]
#
#         print(distance)