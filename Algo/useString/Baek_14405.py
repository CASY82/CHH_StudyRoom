import sys

s = sys.stdin.readline().strip()

s = s.replace("pi", " ")
s = s.replace("ka", " ")
s = s.replace("chu", " ")
s = s.strip()

if s == "":
    print("YES")
else:
    print("NO")