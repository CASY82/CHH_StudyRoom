import sys

gandalf = [1, 2, 3, 3, 4, 10]
sauron = [1, 2, 2, 2, 3, 5, 10]

t = int(sys.stdin.readline())

for no in range(t):
    ga = list(map(int, sys.stdin.readline().split()))
    sa = list(map(int, sys.stdin.readline().split()))

    ga_result = 0
    sa_result = 0

    for i in range(len(gandalf)):
        ga_result += ga[i] * gandalf[i]

    for j in range(len(sauron)):
        sa_result += sa[j] * sauron[j]

    print("Battle {}:".format(no+1), end=" ")

    if ga_result > sa_result:
        print("Good triumphs over Evil")
    elif ga_result == sa_result:
        print("No victor on this battle field")
    else:
        print("Evil eradicates all trace of Good")