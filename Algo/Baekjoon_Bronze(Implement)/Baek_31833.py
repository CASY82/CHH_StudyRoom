import sys

n = int(sys.stdin.readline())
a_list = list(sys.stdin.readline().split())
b_list = list(sys.stdin.readline().split())

a_tmp = int("".join(a_list))
b_tmp = int("".join(b_list))

print(min(a_tmp, b_tmp))