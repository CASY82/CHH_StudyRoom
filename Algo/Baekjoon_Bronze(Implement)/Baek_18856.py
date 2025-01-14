import sys

storage = list(sys.stdin.readline().strip())

if storage.index("@") < storage.index("#") < storage.index("!") or storage.index("@") > storage.index("#") > storage.index("!"):
    print(abs(storage.index("@") - storage.index("!")) - 1)
else:
    print(-1)