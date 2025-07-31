import sys

index = 1
month_str = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split(" ")

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        break

    birth_mon = [0] * 13

    for _ in range(n):
        day, month, year = sys.stdin.readline().strip().split()

        birth_mon[int(month)] += 1

    print("Case #{}:".format(index))
    for i in range(1, 13):
        tmp = ""
        for j in range(birth_mon[i]):
            tmp += "*"
        print("{0}:{1}".format(month_str[i - 1], tmp))

    index += 1