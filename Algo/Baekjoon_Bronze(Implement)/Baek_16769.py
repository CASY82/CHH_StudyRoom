import sys

first_bucket, f_milk = map(int, sys.stdin.readline().split())
second_bucket, s_milk = map(int, sys.stdin.readline().split())
third_bucket, t_milk = map(int, sys.stdin.readline().split())

index = 0

for i in range(100):
    if index % 3 == 0:
        if f_milk + s_milk > second_bucket:
            f_milk = f_milk + s_milk - second_bucket
            s_milk = second_bucket
        else:
            s_milk = f_milk + s_milk
            f_milk = 0
    elif index % 3 == 1:
        if t_milk + s_milk > third_bucket:
            s_milk = t_milk + s_milk - third_bucket
            t_milk = third_bucket
        else:
            t_milk = s_milk + t_milk
            s_milk = 0
    elif index % 3 == 2:
        if f_milk + t_milk > first_bucket:
            t_milk = t_milk + f_milk - first_bucket
            f_milk = first_bucket
        else:
            f_milk = t_milk + f_milk
            t_milk = 0

    index += 1

print(f_milk)
print(s_milk)
print(t_milk)