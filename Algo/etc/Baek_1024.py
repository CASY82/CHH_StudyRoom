# 실패, 수학 문제인 것을 알고나니 허탈했다....
n, l = map(int, input().split())

for i in range(l, 101):
    x = n - (i * (i + 1) / 2)

    if x % i == 0:
        x = int(x / i)

        if x >= -1:
            for j in range(1, i + 1):
                print(x + j, end=' ')
            print()
            break
else:
    print(-1)


# 런타임 에러 발생...
# tmp = n - ((l + 1) * l // 2)
#
# while l <= 100:
#     if tmp % l == 0:
#         num = tmp // l
#         break
#
#     l += 1
#
# for i in range(l):
#     print(num + i, end=' ')

# 2 pointer로 구현했으나 시간 초과
# interval_sum = 1
# end = 1
#
# for start in range(1, (n // 3)):
#     while interval_sum < n:
#         end += 1
#         interval_sum += end
#
#     if interval_sum == n:
#         num_list.append([i for i in range(start, end+1)])
#         interval_sum = 0
#         end = start
#
#     if interval_sum > n:
#         interval_sum -= start
#
# if len(num_list) > 100 or len(num_list) == 0:
#     print('-1')
#
# low_length = 101
# indexer = 0
#
# for i in range(len(num_list)):
#     if len(num_list[i]) < low_length and len(num_list[i]) >= l:
#         low_length = len(num_list[i])
#         indexer = i
#
# for i in num_list[indexer]:
#     print(i, end=' ')

#파이써닉 참고
# N,L=map(int,input().split());c=-1,
# for d in range(100,L-1,-1):a=N-d*~-d//2;c=range(a//d,a//d+(1>a%d<=a)*d)or c
# print(*c)