import sys

play = list(sys.stdin.readline().strip())

a = 0
b = 0
match_point = False

for i in range(0, len(play), 2):
    if play[i] == "A":
        a += int(play[i+1])
    else:
        b += int(play[i+1])

    if a == b == 10:
        match_point = True

    if not match_point:
        if a > b and a >= 11:
            print("A")
            break
        elif b > a and b >= 11:
            print("B")
            break
    else:
        if abs(a-b) >= 2:
            if a > b:
                print("A")
            else:
                print("B")
            break

# 다른 사람 풀이
# score = input()
# score_a = []
# score_b = []
#
# cnt = 0
# for i in range(int(len(score) / 2)):
#     if score[cnt] == 'A':
#         score_a.append(score[cnt:cnt + 2])
#         cnt += 2
#     else:
#         score_b.append(score[cnt:cnt + 2])
#         cnt += 2
#
# A = 0
# B = 0
# for j in score_a:
#     A += int(j[-1])
# for k in score_b:
#     B += int(k[-1])
#
# if max(A, B) == A:
#     print('A')
# else:
#     print('B')