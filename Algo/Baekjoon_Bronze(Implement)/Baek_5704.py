import sys

alpha = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(",")


while True:
    sentences = sys.stdin.readline().strip()
    alpha_cnt = [0 for _ in range(26)]

    if sentences == "*":
        break

    for i in range(26):
        alpha_cnt[i] += sentences.count(alpha[i])

    if 0 in alpha_cnt:
        print("N")
    else:
        print("Y")