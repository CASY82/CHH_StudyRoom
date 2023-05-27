# 시간 초과
# import sys
#
# sentence = sys.stdin.readline().strip()
# bomb = sys.stdin.readline().strip()
#
# stack = []
#
# for i in range(len(sentence)):
#     stack.append(sentence[i])
#
#     if bomb in "".join(stack):
#         for _ in range(len(bomb)):
#             stack.pop()
#
# if len(stack) == 0:
#     print("FRULA")
# else:
#     print("".join(stack))

# 시간 초과 2
# import sys
#
# sentence = sys.stdin.readline().strip()
# bomb = sys.stdin.readline().strip()
#
# stack = []
#
# for i in range(len(sentence)):
#     stack.append(sentence[i])
#     tmp = "".join(stack)
#
#     if bomb in tmp:
#         tmp = tmp.replace(bomb, "")
#         stack = []
#         stack.append(tmp)
#
# if tmp == "":
#     print("FRULA")
# else:
#     print(tmp)

import sys

sentence = sys.stdin.readline().strip()
bomb = sys.stdin.readline().strip()

def remove_pattern(string, pattern):
    stack = []
    pattern_length = len(pattern)

    for char in string:
        stack.append(char)

        if char == pattern[-1] and len(stack) >= pattern_length:
            match = True
            for i in range(pattern_length):
                if stack[-pattern_length + i] != pattern[i]:
                    match = False
                    break

            if match:
                for _ in range(pattern_length):
                    stack.pop()

    result = ''.join(stack)
    return result

tmp = remove_pattern(sentence, bomb)

if len(tmp) == 0:
    print("FRULA")
else:
    print(tmp)