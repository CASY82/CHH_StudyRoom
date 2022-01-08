import sys

t = int(sys.stdin.readline())
dic = dict()
alpha = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(',')

for i in range(len(alpha)):
    dic[alpha[i]] = i+1

for _ in range(t):
    word = sys.stdin.readline().strip().split(" ")
    result = []

    for i in range(len(word[0])):
        num = dic[word[1][i]] - dic[word[0][i]]
        if num < 0:
            num += 26
        result.append(num)

    print("Distances:", end=" ")
    for j in result:
        print(j, end=" ")
    print()