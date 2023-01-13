import sys

alpha = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split()

n = int(sys.stdin.readline())

for _ in range(n):
    word = sys.stdin.readline().strip().replace(" ", "")
    result = 0

    for i in range(len(word)):
        result += alpha.index(word[i])+1

    if result == 100:
        print("PERFECT LIFE")
    else:
        print(result)