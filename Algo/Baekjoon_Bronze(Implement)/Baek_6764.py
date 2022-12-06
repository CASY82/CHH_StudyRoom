import sys

num = []

for _ in range(4):
    num.append(int(sys.stdin.readline()))

up_tmp = num.copy()
down_tmp = num.copy()

up_tmp.sort()
down_tmp.sort(reverse=True)

if len(set(num)) == 1:
    print("Fish At Constant Depth")
elif num == up_tmp and len(set(num)) == 4:
    print("Fish Rising")
elif num == down_tmp and len(set(num)) == 4:
    print("Fish Diving")
else:
    print("No Fish")