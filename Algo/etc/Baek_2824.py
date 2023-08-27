import sys

def GCD(x, y):
    while(y):
        x, y = y, x%y
    return x

n = int(sys.stdin.readline())
first_num_list = list(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
second_num_list = list(map(int, sys.stdin.readline().split()))

first_num = 1
second_num = 1

for fir in first_num_list:
    first_num *= fir

for sec in second_num_list:
    second_num *= sec

tmp = GCD(first_num, second_num)
tmp = str(tmp)

if len(tmp) > 9:
    print(tmp[-9:])
else:
    print(tmp)