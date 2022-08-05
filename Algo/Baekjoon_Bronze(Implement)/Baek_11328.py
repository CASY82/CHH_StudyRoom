import sys

n = int(sys.stdin.readline())

alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")

for _ in range(n):
    origin = [0 for _ in range(26)]
    diff = [0 for _ in range(26)]

    first, second = sys.stdin.readline().strip().split()
    result = True

    for i in range(len(first)):
        origin[alpha.index(first[i])] += 1

    for j in range(len(second)):
        diff[alpha.index(second[j])] += 1

    for i in range(26):
        if origin[i] != diff[i]:
            result = False
            break

    if result:
        print("Possible")
    else:
        print("Impossible")