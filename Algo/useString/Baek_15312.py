import sys

a = sys.stdin.readline().strip()
b = sys.stdin.readline().strip()

alp = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z".split(",")
alp_cnt = [3, 2, 1, 2, 3, 3, 2, 3, 3, 2, 2, 1, 2, 2, 1, 2, 2, 2, 1, 2, 1, 1, 1, 2, 2, 1]

name_sum = ""
tmp = []
tmp2 = []

for i in range(len(a)):
    name_sum += a[i]
    name_sum += b[i]

#수 구하는 로직
for i in range(len(name_sum)):
    tmp.append(alp_cnt[alp.index(name_sum[i])])

while len(tmp) > 2:
    for j in range(len(tmp)-1):
        tmp2.append((tmp[j] + tmp[j+1])%10)

    tmp = tmp2.copy()
    tmp2.clear()

for i in tmp:
    print(i, end="")