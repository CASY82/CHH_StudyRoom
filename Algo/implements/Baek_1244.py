import sys

n = int(sys.stdin.readline())
switch = list(map(int, sys.stdin.readline().split()))
student_num = int(sys.stdin.readline())

# 남학생 1, 여학생 2
# 남학생인 경우 받은 수의 배수 스위치를 스위칭
# 여학생의 경우 받은 수를 기준으로 오, 왼 대칭을 비교하여 가장 많이 같은 상태를 유지하는 스위치를 포함하는 구간을 모두 스위칭

for _ in range(student_num):
    sex, number = map(int, sys.stdin.readline().split())

    if sex == 1:
        for i in range(number - 1, n, number):
            if switch[i] == 1:
                switch[i] = 0
            else:
                switch[i] = 1
    else:
        if switch[number - 1] == 0:
            switch[number - 1] = 1
        else:
            switch[number - 1] = 0
        left, right = number - 2, number
        while left >= 0 and right < n and switch[left] == switch[right]:
            if switch[left] == 0:
                switch[left], switch[right] = 1, 1
            else:
                switch[left], switch[right] = 0, 0
            left = left - 1
            right = right + 1

line = len(switch) // 20 + 1
index = 0

if len(switch) > 20:
    for i in range(line):
        for j in range(20):
            if index >= len(switch):
                break
            print(switch[index], end=" ")
            index += 1

        if index > len(switch):
            break
        print()
else:
    print(*switch)

# 다른 사람 풀이
# import sys
# N = int(sys.stdin.readline())
# switch = [-1] + list(map(int, sys.stdin.readline().split()))
# M = int(sys.stdin.readline())
# for _ in range(M):
#     student, num = map(int, sys.stdin.readline().split())
#     if student == 1 :
#         for i in range(1, N//num+1):
#             if switch[i*num] == 0 :
#                 switch[i*num] = 1
#             else     :
#                 switch[i*num] = 0
#     if student == 2 :
#         if switch[num] == 0:
#             switch[num] = 1
#         else :
#             switch[num] = 0
#         left, right = num-1, num+1
#         while left > 0 and right <= N and switch[left] == switch[right]:
#             if switch[left] == 0:
#                 switch[left], switch[right] = 1,1
#             else :
#                 switch[left], switch[right] = 0,0
#             left = left - 1
#             right = right + 1
# # 출력 조건에 맞춰주자
# for k in range(1,N+1):
#     print(switch[k], end=" ")
#     if k % 20 == 0:
#         print()