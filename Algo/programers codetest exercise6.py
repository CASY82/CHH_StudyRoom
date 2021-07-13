#스택/큐 2번 프린터(결국... 다른 사람들이 푼 답을 보고 푼 문제...)

# [2, 1, 3, 2]
# [3, 1, 3, 3, 1]
# [2, 1, 9, 1, 9, 1]
# [2, 1, 2, 1, 2]
# [1, 1, 1, 1, 1, 1, 1]

priorities = [2, 1, 9, 1, 9, 1]
location = 1

def solution(priorities, location):
  answer = 0
  from collections import deque

  d = deque([(v,i) for i,v in enumerate(priorities)])

  while len(d):
      item = d.popleft() #제일 큰 값은 location의 선택을 받지 못하면 계속 빠져나감
      if d and max(d)[0] > item[0]: #d의 값이 남아있는지 확인 후, d의 우선순위 부분 비교
          d.append(item) #작으면 맨 뒤로 넣어주기
      else:
          answer += 1 #크면 answer를 증가시키고 d의 index부분이 location과 같은지를 비교하여 멈춤
          if item[1] == location:
              break
  return answer


print(solution(priorities, location))






# 첫번째 시도
    # best_pro = 0
    # best_pro_location = 0
    # mover = []
    # count = 0
    #
    # for i in range(len(priorities)):
    #     if best_pro < priorities[i]:
    #         best_pro = priorities[i]
    #         best_pro_location = i
    #
    # for i in range(len(priorities)):
    #     if priorities[0] != best_pro:
    #         mover.append(priorities[0])
    #         priorities.pop(0)
    #         priorities.append(mover[i])
    #         count += 1
    #
    #     if priorities[0] == best_pro:
    #         break
    #
    # if best_pro_location > location:
    #     answer = (len(priorities) - 1) - best_pro_location + count
    # else:
    #     answer = 1




# 2번째 풀이 왜 틀리나 했더니 문제 이해를 완전 잘못하고 있었다
# 우선순위대로 먼저 출력해야된다는 사실을 전혀 인지하지 못하고 푼 방식

# def solution(priorities, location):
#     answer = 0
#     lo_array = [a for a in range(len(priorities))]
#     best_pro = 0
#     best_pro_location = 0
#     mover = []
#     mover_location = []
#
#     for i in range(len(priorities)):
#         if best_pro < priorities[i]:
#             best_pro = priorities[i]
#             best_pro_location = i
#
#     for i in range(len(priorities)):
#         if priorities[0] != best_pro:
#             mover.append(priorities[0])
#             priorities.pop(0)
#             priorities.append(mover[i])
#             mover_location.append(lo_array[0])
#             lo_array.pop(0)
#             lo_array.append(mover_location[i])
#
#         if priorities[0] == best_pro:
#             break
#
#     for i in range(len(priorities)):
#         if location != lo_array[i]:
#             answer += 1
#         else:
#             answer += 1
#             break
#
#     return answer

# 3번째 도전.... 결국 중간 숫자가 있을 때가 문제가 되었다... 무조건 제일 큰 숫자를 앞으로 빼기 위해서 모든 경우를 for를 돌다보니... 제일 작은 숫자들끼리 정렬이 되어버린다...

# def solution(priorities, location):
#     answer = 0
#     lo_array = [a for a in range(len(priorities))]
#     idx = 0
#
#     for i in range(len(priorities)):
#         if max(priorities) > priorities[idx]:
#             priorities.append(priorities.pop(idx))
#             lo_array.append(lo_array.pop(idx))
#         else:
#             if priorities[i] != priorities[i-1]:
#                 idx += 1
#             else:
#                 continue
#
#     for i in range(len(priorities)):
#         if lo_array[i] == location:
#             answer += 1
#             break
#         else:
#             answer += 1
#
#     print(lo_array)
#     print(priorities)
#
#     return answer