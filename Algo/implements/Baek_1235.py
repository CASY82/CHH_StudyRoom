import sys

n = int(sys.stdin.readline())
stuNo = []
result = 0

for _ in range(n):
    stuNo.append(sys.stdin.readline().strip())

#여기 실수...
for i in range(1, len(stuNo[0])+1):
    newNum = []
    for j in range(n):
        newNum.append(stuNo[j][::-1][:i])

    if len(set(newNum)) == n:
        result = i
        break

print(i)