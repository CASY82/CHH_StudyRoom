import sys

word = sys.stdin.readline().strip()

alpha = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")
result = 0

for i in range(len(word)):
    if i > 0:
        result += min(26 - abs(alpha.index(word[i-1])-alpha.index(word[i])), abs(alpha.index(word[i-1])-alpha.index(word[i])))
    else:
        result += min(26 - abs(alpha.index(word[0]) - alpha.index('A')), abs(alpha.index(word[0]) - alpha.index('A')))

print(result)