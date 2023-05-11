import sys

student_dic = dict()

n = int(sys.stdin.readline())
total = int(sys.stdin.readline())
chucheon = list(map(int, sys.stdin.readline().split()))
picture_side = []

for num in chucheon:
    if num in picture_side:
        student_dic[num] += 1
    else:
        if len(picture_side) >= n:
            for i in range(n): #여기 부분 실수 레전드네 진짜;;;
                if min(student_dic.values()) == student_dic[picture_side[i]]:
                    del student_dic[picture_side[i]]
                    picture_side.remove(picture_side[i])
                    break
        picture_side.append(num)
        student_dic[num] = 1

result = list(picture_side)
result.sort()
print(*result)

#계속 틀려서 확인용으로 돌려봅니다.
# N = int(input()) # 사진틀 개수
# Vote = int(input()) # 총 추천 회수
# students = list(map(int, input().split())) # 추천 학생 번호
# picture = [] # 사진틀
# score = [] # 사진틀 인덱스와 매치해서 추천수 저장할 리스트
#
# for i in range(Vote):
#     if students[i] in picture: # 사진틀에 있으면
#         for j in range(len(picture)):
#             if students[i] == picture[j]:
#                 score[j] += 1 #점수증가
#     else: # 사진틀에 없고
#         if len(picture) >= N: # 사진틀 꽉차있으면
#             for j in range(N):
#                 if score[j] == min(score): #가장 작은 점수 찾고
#                     del picture[j]
#                     del score[j]
#                     break #먼저 찾으면 스탑 왜냐면 오래된거일수록 인덱스 앞에 있음
#         picture.append(students[i]) #새로운거 뒤에 더해줌
#         score.append(1)
#
# picture.sort()
# print(' '.join(map(str, picture)))