import sys

n = int(sys.stdin.readline())
jbitecode = sys.stdin.readline().strip()

for word in ("J", "A", "V"):
    if word in jbitecode:
        jbitecode = jbitecode.replace(word, "")

if jbitecode == "":
    print("nojava")
else:
    print(jbitecode)