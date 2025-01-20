import sys

# 범위가 10을 넘지 않아서 이렇게 풀어도 풀림
n = sys.stdin.readline().strip()
point = 0

if n[point] != "1":
    print(-1)
else:
    res = True
    compare_num = 1
    while point < len(n):
        if n[point] == str(compare_num):
            point += 1
            compare_num += 1
        else:
            res = False
            break

    if res:
        print(compare_num - 1)
    else:
        print(-1)

# 다른 사람 풀이
# s = ""
# a = input()
# i = 1
# while(True):
#     s+= str(i)
#     if a==s:
#         print(i)
#         break
#     if len(s)>len(a):
#         print(-1)
#         break
#     i+=1