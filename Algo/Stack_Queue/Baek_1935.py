import sys

n = int(sys.stdin.readline())
alpha = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")
alpha_num = [0 for i in range(26)]
sick = sys.stdin.readline().strip()
stack = []

for i in range(n):
    alpha_num[i] = int(sys.stdin.readline())

for j in range(len(sick)):
    if sick[j] in alpha:
        stack.append(alpha_num[alpha.index(sick[j])])
    else:
        a = stack.pop()
        b = stack.pop()

        if sick[j] == "*":
            result = b*a
        elif sick[j] == "+":
            result = b+a
        elif sick[j] == "-":
            result = b-a
        else:
            result = b/a

        stack.append(result)

print('%0.2f' % stack[0])