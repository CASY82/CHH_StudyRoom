import sys

firC, firP = map(int, sys.stdin.readline().split())
secC, secP = map(int, sys.stdin.readline().split())

def Euclid(a, b):
    if a % b == 0:
        return b

    else:
        return Euclid(b, a % b)

#분수를 만들고
resultP = (firP * secP) // Euclid(firP, secP)
resultC = firC * (resultP // firP) + secC * (resultP // secP)

#기약 분수로 나타낸다... 까먹음
tmp = Euclid(resultC, resultP)
print(resultC // tmp, resultP // tmp)