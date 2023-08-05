import sys
import re

word = sys.stdin.readline().strip()
pattern = "ss"

result = re.search(pattern, word)

if result:
    print("hiss")
else:
    print("no hiss")