#딕셔너리가 더 빠르긴 할듯?
import sys

word = sys.stdin.readline().strip()

alpha = "a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(',')
count = [0 for i in range(26)]

for i in alpha:
    count[alpha.index(i)] += word.count(i)

for i in count:
    print(i, end=' ')