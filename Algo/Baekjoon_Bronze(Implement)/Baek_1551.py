n, k = map(int, input().split())

num = list(map(int, input().split(',')))

def make_num_list(num):
    new_num = []
    for i in range(len(num) - 1):
        new_num.append(num[i+1] - num[i])

    return new_num

tmp = num

for _ in range(k):
    tmp = make_num_list(tmp)

for i in range(len(tmp)):
    print(tmp[i], end='')
    if len(tmp)-1 != i:
        print(',', end='')

#출력 부분 참고

# def reduce(li):
#     return [a - b for a, b in zip(li[1:], li[:-1])]
#
#
# n, k = map(int, input().split())
# li = list(map(int, input().split(',')))
#
# for _ in range(k):
#     li = reduce(li)
#
# print(','.join(map(str, li)))