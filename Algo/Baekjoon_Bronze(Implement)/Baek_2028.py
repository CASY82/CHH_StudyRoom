t = int(input())

for i in range(t):
    n = int(input())

    double_n = str(n * n)
    n_str = str(n)
    check = []

    for j in range(len(n_str)):
        if n_str[len(n_str) - 1 - j] == double_n[len(double_n) - 1 - j]:
            check.append(1)
        else:
            check.append(0)

    if min(check) == 1:
        print("YES")
    else:
        print("NO")