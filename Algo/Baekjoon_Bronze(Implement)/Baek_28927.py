import sys

t1, e1, f1 = map(int, sys.stdin.readline().split())
t2, e2, f2 = map(int, sys.stdin.readline().split())

watch_max = t1 * 3 + e1 * 20 + f1 * 120
watch_mel = t2 * 3 + e2 * 20 + f2 * 120

if watch_mel > watch_max:
    print("Mel")
elif watch_mel < watch_max:
    print("Max")
else:
    print("Draw")