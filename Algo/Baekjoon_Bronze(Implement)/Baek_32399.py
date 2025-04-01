import sys

hamberger = sys.stdin.readline().strip()

tmp = {
    "(1)": 0,
    ")1(": 2
}

if hamberger in tmp:
    print(tmp[hamberger])
else:
    print(1)

# 다른 사람 풀이

# a=input()
# cnt=0
# while True:
#     if '(1)' in a:
#         print(0)
#         break
#     elif '1)' in a:
#         print(1)
#         break
#     elif '(1' in a:
#         print(1)
#         break
#     elif '()' in a:
#         print(1)
#         break
#     else:
#         print(2)
#         break