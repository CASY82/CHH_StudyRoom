# 스택/큐 1번 기능개발

# def solution(progresses, speeds):
#     answer = []
    # count = 0
    # i = 0
    # progresses = progresses[::-1]
    # speeds = speeds[::-1]
    #
    #
    # while True:
    #     progresses[i] += speeds[i]
    #
    #     if progresses[-1] >= 100:
    #         progresses.pop()
    #         speeds.pop()
    #         count += 1
    #
    #     if i > len(progresses):
    #         answer.append(count)
    #         i = 0
    #
    #     if not progresses:
    #         break

    # return answer

import math

#[95, 90, 99, 99, 80, 99]
#[1, 1, 1, 1, 1, 1]

#[93, 30, 55]
#[1, 30, 5]

#[21, 25, 20]
#[5, 5, 5]

progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]

def solution(progresses, speeds):
    anwser = []
    stack = []
    tmp = 0
    top = 0
    count = 1

    for i in range(len(progresses)):
        tmp = math.ceil((100 - progresses[i]) / speeds[i])
        stack.append(tmp)


    stack_re = stack[::-1]
    top = stack_re[len(stack_re)-1]

    while True:
        last_num = len(stack_re) - 2

        if last_num < 0:
            anwser.append(count)
            break

        if top >= stack_re[last_num]:
            count += 1
            stack_re.pop()
        else:
            top = stack_re[last_num]
            anwser.append(count)
            count = 1
            stack_re.pop()

    return anwser


print(solution(progresses, speeds))

#드디어 처음으로 혼자힘으로 풀었다! 하지만 코드가 너무 길고 아직 부족하다.....

#Queue를 이용한 풀이

# def solution(progresses, speeds):
#     answer = []
#     time = 0
#     count = 0
#
#     while len(progresses) > 0:
#         if (progresses[0] + time * speeds[0]) >= 100:
#             progresses.pop(0)
#             speeds.pop(0)
#             count += 1
#
#         else:
#             if count > 0:
#                 answer.append(count)
#                 count = 0
#             time += 1
#     answer.append(count)
#     return answer

# math.ceil을 이용한 풀이
# import math
#
#
# def solution(progresses, speeds):
#     progresses = [math.ceil((100 - a) / b) for a, b in zip(progresses, speeds)]
#     answer = []
#     front = 0, 0
#
#     for idx in range(len(progresses)):
#         if progresses[idx] > progresses[front]:
#             answer.append(idx - front)
#             front = idx
#     answer.append(len(progresses) - front)
#
#     return answer