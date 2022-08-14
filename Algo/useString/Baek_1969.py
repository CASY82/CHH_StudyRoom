import sys

n, m = map(int, sys.stdin.readline().split())

dna = []
many_dna = []
result = 0

for _ in range(n):
    dna.append(sys.stdin.readline().strip())

for i in range(m):
    tmp = []
    newcleo = set()

    for j in range(n):
        tmp.append(dna[j][i])
        newcleo.add(dna[j][i])

    tmp_newcleo = list(newcleo)
    cnt = [0 for _ in range(len(tmp_newcleo))]

    for dna_li in range(len(tmp_newcleo)):
        t_cnt = tmp.count(tmp_newcleo[dna_li])

        cnt[dna_li] = t_cnt

    tmp2 = []

    for k in range(len(tmp_newcleo)):
        if max(cnt) == cnt[k]:
            tmp2.append(tmp_newcleo[k])

    tmp2.sort()

    for last in tmp:
        if tmp2[0] != last:
            result += 1

    many_dna.append(tmp2[0])

print("".join(many_dna))
print(result)