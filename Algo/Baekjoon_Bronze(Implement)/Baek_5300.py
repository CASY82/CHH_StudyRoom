import sys

n = int(sys.stdin.readline())

namuzi = n % 6

for i in range(1, n-namuzi+1):
    print(i, end=" ")

    if i != 0 and i % 6 == 0:
        print("Go!", end=" ")

if namuzi > 0:
    for j in range(namuzi):
        print(n-namuzi + j + 1, end=" ")

    print("Go!", end=" ")