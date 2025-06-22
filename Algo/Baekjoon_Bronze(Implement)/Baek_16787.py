N = int(input())
S = input().strip()
used = [False] * N
res = 0

for i in range(N - 1):
    if not used[i] and not used[i + 1] and (S[i:i+2] == 'OX' or S[i:i+2] == 'XO'):
        used[i] = used[i + 1] = True
        res += 1

print(res)