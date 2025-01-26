import sys

n = int(sys.stdin.readline())
s = list(sys.stdin.readline().strip())
t = list(sys.stdin.readline().strip())

s_win = 0
t_win = 0

for i in range(n):
    if s[i] == "R" and t[i] == "P":
        t_win += 1
    elif s[i] == "S" and t[i] == "P":
        s_win += 1
    elif s[i] == "S" and t[i] == "R":
        t_win += 1

print(s_win, t_win)