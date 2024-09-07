import sys

alpha = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")

word = sys.stdin.readline().strip()
res = ""
index = 0

while index < len(word):
    res += word[index]
    index += alpha.index(word[index]) + 1

print(res)

# 다른 사람 풀이
# s = input()
# ans = ""
# num = 0
# while  num <len(s):
#     ans += s[num]
#     cnt = ord(s[num])-ord('A')+1
#     num += cnt
# print(ans)