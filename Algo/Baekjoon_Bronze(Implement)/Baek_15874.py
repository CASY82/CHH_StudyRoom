import sys

alpha = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")
alpha_small = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")

k, s = map(int, sys.stdin.readline().split())
sentence = list(sys.stdin.readline().strip())

res = []

for i in range(len(sentence)):
    if sentence[i] in alpha:
        res.append(alpha[(alpha.index(sentence[i]) + k) % 26])
    elif sentence[i] in alpha_small:
        res.append(alpha_small[(alpha_small.index(sentence[i]) + k) % 26])
    else:
        res.append(sentence[i])

print("".join(res))