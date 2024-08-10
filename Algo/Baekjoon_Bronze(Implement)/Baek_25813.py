import sys

def makeString(idx, word):
    tmp = ""

    for _ in range(idx):
        tmp += word

    return tmp

word = sys.stdin.readline().strip()
ans = ""
f_index = 0
u_index = 0
u_check = True

for alpha in range(len(word)):
    if word[alpha] == "U" and u_check:
        u_index = alpha
        u_check = False
    elif word[alpha] == "F":
        f_index = alpha

ans += makeString(u_index, "-")
ans += "U"
ans += makeString(f_index - u_index - 1, "C")
ans += "F"
ans += makeString(len(word) - f_index - 1, "-")

print(ans)