import sys

t = int(sys.stdin.readline())

alpha = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")

def Affine_Cipher(a, b, X):
    tmp = alpha.index(X)

    affine = (a * tmp + b) % 26

    return alpha[affine]


for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    word = sys.stdin.readline().strip()
    result = ''

    for i in range(len(word)):
        result += Affine_Cipher(a, b, word[i])

    print(result)