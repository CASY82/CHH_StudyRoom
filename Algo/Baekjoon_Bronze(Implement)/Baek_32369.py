import sys

n, a, b = map(int, sys.stdin.readline().split())

good_onion = 1
bad_onion = 1

for i in range(n):
    good_onion += a
    bad_onion += b

    if good_onion < bad_onion:
        good_onion, bad_onion = bad_onion, good_onion
    elif good_onion == bad_onion:
        bad_onion -= 1

print(good_onion, bad_onion)