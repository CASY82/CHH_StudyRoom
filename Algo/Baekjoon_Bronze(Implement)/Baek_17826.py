import sys

score = list(map(int, sys.stdin.readline().split()))
my_score = int(sys.stdin.readline())

score.append(my_score)
score.sort(reverse=True)
res = score.index(my_score) + 1

if 1 <= res <= 5:
    print("A+")
elif 6 <= res <= 15:
    print("A0")
elif 16 <= res <= 30:
    print("B+")
elif 31 <= res <= 35:
    print("B0")
elif 36 <= res <= 45:
    print("C+")
elif 46 <= res <= 48:
    print("C0")
elif 49 <= res <= 50:
    print("F")

# 다른 사람 풀이
# arr = list(map(int, input().split()))
# score = int(input())
# idx = -1
# for i in range(len(arr)):
#     if arr[i]==score :
#         idx = i+1
#         break
# if idx<=5 : print('A+')
# elif idx<=15 : print('A0')
# elif idx<=30 : print('B+')
# elif idx<=35 : print('B0')
# elif idx<=45 : print('C+')
# elif idx<=48 : print('C0')
# else : print('F')