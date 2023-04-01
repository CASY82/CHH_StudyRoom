import sys

n = int(sys.stdin.readline())
hello = set()
result = 0

for _ in range(n):
    chatting = sys.stdin.readline().strip()

    if chatting == "ENTER":
        result += len(hello)
        hello.clear()
    else:
        hello.add(chatting)

result += len(hello)
print(result)

# 다른 사람 풀이 --> 명맥은 같네
# import sys
# input = sys.stdin.readline
#
# n = int(input())
# s = set()
# ret = 0
# for _ in range(n):
#     chat = input().rstrip()
#     if chat == "ENTER":
#         ret += len(s)
#         s = set()
#     else:
#         s.add(chat)
# ret += len(s)
# print(ret)