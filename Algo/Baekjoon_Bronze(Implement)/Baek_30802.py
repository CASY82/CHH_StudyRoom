import sys

n = int(sys.stdin.readline())
t_shirts = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())

shirts_dummy = 0

for i in t_shirts:
    if i % t == 0:
        shirts_dummy += i // t
    else:
        shirts_dummy += (i // t) + 1

print(shirts_dummy)
print(n // p, n % p)