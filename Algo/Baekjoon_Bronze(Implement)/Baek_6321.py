import sys

alpha = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z A".split(" ")

n = int(sys.stdin.readline())

for i in range(n):
    word = list(sys.stdin.readline().strip())
    result = ""

    for j in range(len(word)):
        result += alpha[alpha.index(word[j])+1]

    print("String #{0}".format(i + 1))
    print(result)
    print()