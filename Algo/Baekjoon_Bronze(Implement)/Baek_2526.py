n, p = map(int, input().split())

num = n
num_list = []
recur_list = []

while True:
    num = (num * n) % p
    if num in num_list:
        if num in recur_list:
            break
        recur_list.append(num)


    num_list.append(num)

print(len(recur_list))