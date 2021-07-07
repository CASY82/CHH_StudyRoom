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
#드디어 처음으로 혼자힘으로 풀었다! 하지만 코드가 너무 길고 아직 부족하다.....

print(solution(progresses, speeds))