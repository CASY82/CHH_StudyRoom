# 공통교육과정

import sys

subject = sys.stdin.readline().strip()

if subject[0] == "F":
    print("Foundation")
elif subject[0] == "C":
    print("Claves")
elif subject[0] == "V":
    print("Veritas")
else:
    print("Exploration")