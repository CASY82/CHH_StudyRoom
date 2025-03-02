import sys
import re

n = int(sys.stdin.readline())
ps = sys.stdin.readline().strip()

while "PS4" in ps or "PS5" in ps:
    ps = re.sub(r'PS[45]', 'PS', ps)

print(ps)