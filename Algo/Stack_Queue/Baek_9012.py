import sys
t = int(sys.stdin.readline())

for _ in range(t):
    vps = list(sys.stdin.readline().strip())
    check = []

    while True:
        if not vps:
            break

        if vps[len(vps) - 1] == "(":
            check.append(vps.pop())
        elif vps[len(vps) - 1] == ")":
            check.append(vps.pop())

        if len(check) >= 2:
            if check[len(check) - 2] == ")" and check[len(check) - 1] == "(":
                check.pop()
                check.pop()

    if not check:
        print("YES")
    else:
        print("NO")

# 갯수를 세는 방법으로 푸는 풀이 발견
# import sys
#
# n = int(sys.stdin.readline())
#
# for i in range(n):
#     vps = sys.stdin.readline().strip()
#     count = 1
#     for j in vps:
#         if(j == '('):
#             count += 1
#         else:
#             count -= 1
#         if(count == 0):
#             break
#     if(count == 1):
#         print("YES")
#     else:
#         print("NO")