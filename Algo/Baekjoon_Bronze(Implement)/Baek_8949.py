import sys

a, b = sys.stdin.readline().strip().split()

al = list(a)
bl = list(b)

al.reverse()
bl.reverse()

tmp = []
for i in range(min(len(al), len(bl))):
    tmp.append(str(int(al[i]) + int(bl[i])))

for j in range(min(len(al), len(bl)), max(len(al), len(bl))):
    if len(al) > len(bl):
        tmp.append(al[j])
    else:
        tmp.append(bl[j])

tmp.reverse()
print("".join(tmp))
