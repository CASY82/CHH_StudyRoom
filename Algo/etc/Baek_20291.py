import sys

n = int(sys.stdin.readline())
extension = dict()

for _ in range(n):
    filetmp = sys.stdin.readline().strip().split(".")

    if filetmp[-1] in extension:
        extension[filetmp[-1]] += 1
    else:
        extension[filetmp[-1]] = 1

for ext, cnt in sorted(extension.items()):
    print(ext, cnt)