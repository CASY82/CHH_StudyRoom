import sys

t = int(sys.stdin.readline())

alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")

for _ in range(t):
    setense = sys.stdin.readline().strip().lower()
    result = []

    for alp in alpha:
        if setense.count(alp) < 1:
            result.append(alp)

    if len(result) == 0:
        print("pangram")
    else:
        print("missing", "".join(result))