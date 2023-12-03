import sys

words = sys.stdin.readline().strip()

alpha_set = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")

for i in range(26):
    if alpha_set[i] not in words:
        print(alpha_set[i])
        break