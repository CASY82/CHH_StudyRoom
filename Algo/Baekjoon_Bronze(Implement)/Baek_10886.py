import sys

n = int(sys.stdin.readline())
cute = 0
no_cute = 0

for _ in range(n):
    survey = int(sys.stdin.readline())

    if survey == 0:
        no_cute += 1
    else:
        cute += 1

if cute > no_cute:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")