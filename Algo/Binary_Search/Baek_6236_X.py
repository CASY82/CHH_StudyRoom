import sys

n, m = map(int, sys.stdin.readline().split())
money = []

for _ in range(n):
    money.append(int(sys.stdin.readline()))

start = 1
end = sum(money)

while start <= end:
    mid = (start + end) // 2
    useMoney = mid
    cnt = 1

    for i in money:
        #이 부분까지는 이해함.. 하지만  '사용할 금액보다 많더라도 남은 금액은 통장에 집어넣고 다시 K원을 인출' 이걸 몰라서
        if useMoney < i:
            useMoney = mid
            cnt += 1
        useMoney -= i

    # 위의 경우를 처리할 수 있는 if 부분을 힌트를 받았다...
    if cnt > m or mid < max(money):
        start = mid + 1
    else:
        end = mid - 1

print(start)