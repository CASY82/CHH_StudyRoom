#너무 문제가 지저분하다
n = int(input())
yeomgi = list(input())

while len(yeomgi) != 1:
    i = len(yeomgi)-1

    if (yeomgi[i-1] == 'A' and yeomgi[i] == 'G') or (yeomgi[i-1] == 'G' and yeomgi[i] == 'A'):
        yeomgi[i - 1] = 'C'
    elif (yeomgi[i-1] == 'A' and yeomgi[i] == 'C') or (yeomgi[i-1] == 'C' and yeomgi[i] == 'A'):
        yeomgi[i - 1] = 'A'
    elif (yeomgi[i-1] == 'A' and yeomgi[i] == 'T') or (yeomgi[i-1] == 'T' and yeomgi[i] == 'A'):
        yeomgi[i - 1] = 'G'
    elif (yeomgi[i-1] == 'G' and yeomgi[i] == 'C') or (yeomgi[i-1] == 'C' and yeomgi[i] == 'G'):
        yeomgi[i - 1] = 'T'
    elif (yeomgi[i-1] == 'G' and yeomgi[i] == 'T') or (yeomgi[i-1] == 'T' and yeomgi[i] == 'G'):
        yeomgi[i - 1] = 'A'
    elif (yeomgi[i-1] == 'C' and yeomgi[i] == 'T') or (yeomgi[i-1] == 'T' and yeomgi[i] == 'C'):
        yeomgi[i - 1] = 'G'

    yeomgi.pop()

print(yeomgi[0])

#숏코딩...???

# import functools as f
# g=lambda l:{v:w for v,w in zip('AGCT',l)}
# d=g([g('ACAG'),g('CGTA'),g('ATCG'),g('GAGT')])
# input();print(f.reduce(lambda v,w:d[v][w],reversed(input())))