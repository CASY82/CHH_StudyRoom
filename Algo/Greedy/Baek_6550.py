import sys

while True:
    try:
        s,t = sys.stdin.readline().strip().split()
    except:
        break

    j = 0
    check = [0 for _ in range(len(s))]

    for i in range(len(t)):
        if j == len(s):
            break
        if t[i] == s[j]:
            check[j] = 1
            j += 1

    if sum(check) == len(s):
        print("Yes")
    else:
        print("No")