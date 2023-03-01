import sys

alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")
number = "1 2 3 4 5 6 7 8 9 0".split(" ")

sentence = list(sys.stdin.readline().strip())

for i in range(len(sentence)):
    if sentence[i] in alpha:
        print(str(alpha.index(sentence[i])+1).zfill(2), end="")
    elif sentence[i] in number:
        print("#{}".format(sentence[i]), end="")
    else:
        print(sentence[i], end="")