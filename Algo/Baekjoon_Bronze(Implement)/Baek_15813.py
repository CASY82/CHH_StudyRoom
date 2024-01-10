import sys

n = int(sys.stdin.readline())

score = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")
total = 0

word = sys.stdin.readline().strip()

for i in range(len(word)):
    total += score.index(word[i]) + 1

print(total)