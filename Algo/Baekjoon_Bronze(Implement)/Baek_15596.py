a = [2, 5, 7]

def sum_num(a):
    sum = 0

    for i in range(len(a)):
        sum += a[i]

    return sum

print(sum_num(a))