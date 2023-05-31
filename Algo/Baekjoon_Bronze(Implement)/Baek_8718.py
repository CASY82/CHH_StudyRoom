import sys

l = int(sys.stdin.readline())
word = sys.stdin.readline().strip()

alpha = "a b c d e f g h i j k l m n o p q r s t u v w x y z".split(" ")
hash_num = []
result = 0

for i in range(len(word)):
    hash_num.append(alpha.index(word[i])+1)

for j in range(l):
    result += hash_num[j] * (31 ** j) % 1234567891

result %= 1234567891

print(result)