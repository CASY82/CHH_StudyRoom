import sys
import re

origin = sys.stdin.readline().strip()
find = sys.stdin.readline().strip()

only_string = re.sub(r'[0-9]+', '', origin)

if find in only_string:
    print(1)
else:
    print(0)