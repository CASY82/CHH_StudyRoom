import sys

alpha = "A B C D E F G H I J K L M N O P Q R S T U V W X Y Z".split(" ")

code = sys.stdin.readline().strip()
code = code[4:] + code[:4]

tmp = ""

for i in range(len(code)):
    if code[i] in alpha:
        tmp += str(alpha.index(code[i]) + 10)
    else:
        tmp += code[i]

if int(tmp) % 97 == 1:
    print("correct")
else:
    print("incorrect")