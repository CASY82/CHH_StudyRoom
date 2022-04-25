import sys

alpha = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")
caesar = "D E F G H I J K L M N O P Q R S T U V W X Y Z A B C".split(" ")

word = sys.stdin.readline().strip()
result = ""

for i in range(len(word)):
    result += alpha[caesar.index(word[i])]

print(result)