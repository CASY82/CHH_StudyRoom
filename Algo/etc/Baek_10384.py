import sys

t = int(sys.stdin.readline())

for k in range(t):
    pangram = {'a' : 0, 'b' : 0, 'c' : 0, 'd' : 0, 'e' : 0, 'f' : 0, 'g' : 0, 'h' : 0, 'i' : 0, 'j' : 0, 'k' : 0, 'l' : 0, 'm' : 0, 'n' : 0, 'o' : 0, 'p' : 0, 'q' : 0, 'r' : 0, 's' : 0, 't' : 0, 'u' : 0, 'v' : 0, 'w' : 0, 'x' : 0, 'y' : 0, 'z' : 0}

    sentense = input()
    sentense = sentense.lower()

    for i in range(len(sentense)):
        if sentense[i] in pangram:
            pangram[sentense[i]] += 1

    tmp = list(pangram.values())
    minVal = 999999999

    for j in range(len(tmp)):
        if minVal > tmp[j]:
            minVal = tmp[j]

    if minVal >= 3:
        print("Case ", k+1, ":", " Triple pangram!!!", sep="")
    elif minVal >= 2:
        print("Case ", k+1, ":", " Double pangram!!", sep="")
    elif minVal >= 1:
        print("Case ", k+1, ":", " Pangram!", sep="")
    else:
        print("Case ", k+1, ":", " Not a pangram", sep="")