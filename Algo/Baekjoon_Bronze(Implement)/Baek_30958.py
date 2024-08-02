import sys

n = int(sys.stdin.readline())
sentence = sys.stdin.readline().strip()
alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
tmp = []

for word in alpha:
    tmp.append((word, sentence.count(word)))

tmp.sort(key=lambda x:x[1])

print(tmp[-1][1])