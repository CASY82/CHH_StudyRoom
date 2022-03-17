import sys

s_length = int(sys.stdin.readline())
s = sys.stdin.readline().strip()

if s.count("2") > s.count("e"):
    print("2")
elif s.count("2") < s.count("e"):
    print("e")
else:
    print("yee")