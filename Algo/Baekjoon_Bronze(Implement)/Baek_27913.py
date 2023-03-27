import sys

n, q = map(int, sys.stdin.readline().split())

tmp_string = 'SciComLove'
string_arr = []

for i in range(n):
    string_arr.append(tmp_string[i%10])

if n % 10 >= 7:
    sub = 3
elif n % 10 >= 4:
    sub = 2
elif n % 10 >= 1:
    sub = 1
else:
    sub = 0

cnt = (n // 10) * 3 + sub

for i in range(q):
    changer = int(sys.stdin.readline())

    if ord(string_arr[changer-1]) < 95:
        string_arr[changer-1] = string_arr[changer-1].lower()
        cnt -= 1
    else:
        string_arr[changer - 1] = string_arr[changer - 1].upper()
        cnt += 1

    print(cnt)


# 다른 사람 풀이

# import sys
# input=sys.stdin.readline
# n, q = map(int, input().split())
# s = "SciComLove" * (n // 10)
# s += "SciComLove"[:n%10]
# cnt = s.count("S") + s.count("C") + s.count("L")
#
# for i in range(q):
#     x = int(input())
#     if s[x - 1].isupper():
#         cnt -= 1
#         s = s[:x - 1] + s[x - 1].lower() + s[x:]
#     else:
#         cnt += 1
#         s = s[:x - 1] + s[x - 1].upper() + s[x:]
#     print(cnt)