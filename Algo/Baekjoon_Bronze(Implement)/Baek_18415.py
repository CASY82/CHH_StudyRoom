import sys
import re

n = int(sys.stdin.readline())
pro = sys.stdin.readline().strip()

pattern = re.compile("joi", re.IGNORECASE)
result = pattern.sub(lambda m: m.group(0).upper(), pro)

print(result)