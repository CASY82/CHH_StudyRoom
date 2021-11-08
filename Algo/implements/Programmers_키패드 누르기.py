# 참고 없이 혼자 풀었다~
# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = "right"

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# hand = "right"

result = "LRLLRRLLLRR"

def solution(numbers, hand):
    answer = ''

    right_only = [3, 6, 9]
    left_only = [1, 4, 7]
    mid = [2, 5, 8, 0]
    right_hand = 12
    left_hand = 10

    for i in numbers:
        count_r = 0
        count_l = 0

        if i in right_only:
            right_hand = i
            answer += 'R'
        elif i in left_only:
            left_hand = i
            answer += 'L'
        else:
            if i in mid:
                if i == 0:
                    i = 11

                tmp_r = abs(right_hand - i)
                tmp_l = abs(left_hand - i)

                count_r = (tmp_r // 3) + (tmp_r % 3)
                count_l = (tmp_l // 3) + (tmp_l % 3)

                if count_l > count_r:
                    right_hand = i
                    answer += 'R'
                elif count_l < count_r:
                    left_hand = i
                    answer += 'L'
                else:
                    if hand == 'left':
                        left_hand = i
                        answer += 'L'
                    else:
                        right_hand = i
                        answer += 'R'

    return answer

print(solution(numbers, hand))
print(result)

#딕셔너리 사용. 다른 사람 풀이
# def solution(numbers, hand):
#     answer = ''
#     key_dict = {1:(0,0),2:(0,1),3:(0,2),
#                 4:(1,0),5:(1,1),6:(1,2),
#                 7:(2,0),8:(2,1),9:(2,2),
#                 '*':(3,0),0:(3,1),'#':(3,2)}
#
#     left = [1,4,7]
#     right = [3,6,9]
#     lhand = '*'
#     rhand = '#'
#     for i in numbers:
#         if i in left:
#             answer += 'L'
#             lhand = i
#         elif i in right:
#             answer += 'R'
#             rhand = i
#         else:
#             curPos = key_dict[i]
#             lPos = key_dict[lhand]
#             rPos = key_dict[rhand]
#             ldist = abs(curPos[0]-lPos[0]) + abs(curPos[1]-lPos[1])
#             rdist = abs(curPos[0]-rPos[0]) + abs(curPos[1]-rPos[1])
#
#             if ldist < rdist:
#                 answer += 'L'
#                 lhand = i
#             elif ldist > rdist:
#                 answer += 'R'
#                 rhand = i
#             else:
#                 if hand == 'left':
#                     answer += 'L'
#                     lhand = i
#                 else:
#                     answer += 'R'
#                     rhand = i
#
#     return answer