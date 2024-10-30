import sys

n, h, w = map(int, sys.stdin.readline().split())
split_word = []
result = ""

for j in range(h):
    words = sys.stdin.readline().strip()
    for i in range(n):
        split_word.append(words[w * i: w * (i + 1)])

for i in range(n):
    check = False
    for j in range(h):
        for k in range(w):
            if split_word[i + j * n][k] != "?":
                result += split_word[i + j * n][k]
                check = True
                break

        if check:
            break

    if not check:
        result += "?"

print(result)

# 다른 사람 풀이
# from sys import stdin
#
# f = stdin.readline
# N, H, W = map(int, f().split())
# l = [f().rstrip() for _ in range(H)]
# ans = []
# for i in range(0, N*W, W):
#   s = ''.join(''.join(e) for e in zip(*[l[j][i:i+W] for j in range(H)]))
#   s = s.replace('?', '')
#   ans.append(s[0] if s else '?')
# print(''.join(ans))