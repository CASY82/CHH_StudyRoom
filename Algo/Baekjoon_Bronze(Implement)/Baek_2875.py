n, m, k = map(int, input().split())
team = 0

while k != 0:
    if k > 0:
         if n < (m * 2):
             m -= 1
             k -= 1
         else:
             n -= 1
             k -= 1

n //= 2
print(min(m, n))