import sys
import re

n = int(sys.stdin.readline())
pattern_arr = sys.stdin.readline().strip().split('*')

pattern = "^" + pattern_arr[0] + "([a-z])*" + pattern_arr[1] + "$"
matcher = re.compile(pattern)

for _ in range(n):
    word = sys.stdin.readline().strip()

    tmp = matcher.match(word)

    if tmp:
        print("DA")
    else:
        print("NE")