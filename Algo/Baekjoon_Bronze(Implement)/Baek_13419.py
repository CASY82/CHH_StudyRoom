import sys

n = int(sys.stdin.readline())

for _ in range(n):
    words = sys.stdin.readline().strip()
    length = len(words)

    if length > 1:
        starter_set = [words[0]]
        ender_set = [words[1]]

        i = 2

        while words[i % length] not in starter_set or words[(i + 1) % length] not in ender_set:
            starter_set.append(words[i % length])
            ender_set.append(words[(i + 1) % length])
            i += 2

        print("".join(starter_set))
        print("".join(ender_set))

    else:
        print(words)
        print(words)

# 다른 사람 풀이

# import sys
#
# t = int(sys.stdin.readline())
#
# for _ in range(t):
#     s = sys.stdin.readline().strip()
#     if len(s) % 2 == 0:
#         print(s[::2])
#         print(s[1::2])
#     else:
#         print(s[::2] + s[1::2])
#         print(s[1::2] + s[::2])