import sys

name = sys.stdin.readline().strip()

outside, _, right = name.partition("(")
inside = right.rstrip(")")

if inside == "":
    inside = "-"

print(outside)
print(inside)