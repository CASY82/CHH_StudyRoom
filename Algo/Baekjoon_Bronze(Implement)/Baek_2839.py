#dp로 풀려했지만 실패.. 그래서 수학 공식으로 그냥 풀었다
n = int(input())

result = float('inf')
check = True
for i in range(n):
    for j in range(n):
        num = 3 * i + 5 * j
        if num > n:
            break

        if num == n:
            result = min(i + j, result)
            check = False

if check:
    print(-1)
else:
    print(result)