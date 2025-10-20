import sys

s_cost, s_weight = map(int, sys.stdin.readline().split())
n_cost, n_weight = map(int, sys.stdin.readline().split())
u_cost, u_weight = map(int, sys.stdin.readline().split())

s_weight *= 10
n_weight *= 10
u_weight *= 10
s_cost *= 10
n_cost *= 10
u_cost *= 10

if s_cost >= 5000:
    s_cost -= 500

if n_cost >= 5000:
    n_cost -= 500

if u_cost >= 5000:
    u_cost -= 500

sg = s_weight / s_cost
ng = n_weight / n_cost
ug = u_weight / u_cost

tmp = max(sg, ng, ug)

if tmp == sg:
    print("S")
elif tmp == ng:
    print("N")
else:
    print("U")