import sys

history = []

while True:
    number = int(sys.stdin.readline())

    if number == 0:
        break

    answer = sys.stdin.readline().strip()

    if answer == "right on":
        tmp = number
        check = True

        for com_num, com_ans in history:
            if (com_num <= tmp and com_ans == "too high") or (com_num >= tmp and com_ans == "too low"):
                check = False
                break

        if check:
            print("Stan may be honest")
        else:
            print("Stan is dishonest")

        history = []
    else:
        history.append((number, answer))

# 다른 사람 풀이
# l=0;h=11
# while n:=int(input()):
#     c=input()[4]
#     if c=='h':h=min(h,n)
#     elif c=='l':l=max(l,n)
#     else:print('Stan',['is dishonest','may be honest'][l<n<h]);l=0;h=11

# 다른 사람 풀이2
# up_limit = 11
# down_limit = 0
# while True:
#     n = int(input())
#     if n == 0:
#         break
#
#     answer = input()
#     if answer == "too high":
#         if up_limit > n:
#             up_limit = n
#     elif answer == "too low":
#         if down_limit < n:
#             down_limit = n
#     else:
#         if not (down_limit < n < up_limit):
#             print("Stan is dishonest")
#         else:
#             print("Stan may be honest")
#         up_limit = 11
#         down_limit = 0
