import sys

alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
alpha = [""] + alpha

n = int(sys.stdin.readline())
s = sys.stdin.readline().strip()
weight = 0

if len(s) > n:
    print("Impossible")
else:
    for i in range(len(s)):
        weight += alpha.index(s[i])

    print(weight)