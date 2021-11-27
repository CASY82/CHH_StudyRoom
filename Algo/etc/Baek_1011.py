#규칙을 찾아서 수학으로 풀어내었다!!!!! 규칙 찾는데는 약간의 참고사항이 있었지만 로직자체는 순수하게 생각해서 푼 첫 골드문제!!!
t = int(input())

for _ in range(t):
    x, y = map(int, input().split())

    i = 0
    distance = y - x
    want_val = 0

    while True:
        if i * (i + 1) < distance and (i + 1) * (i + 2) >= distance:
            want_val = i + 1
            first = i * (i + 1)
            second = (i + 1) * (i + 2)
            break

        i += 1

    # print(want_val)
    stand = (first + second) // 2
    if stand >= distance:
        print(want_val * 2 - 1)
    else:
        print(want_val * 2)

# exam
# 입력:
# 15
# 0 15
# 20 23
# 0 2147483647
# 1 2147483647
# 2 2147483647
# 41706 2147483647
# 41707 2147483647
# 2147483643 2147483647
# 2147483644 2147483647
# 2147483645 2147483647
# 2147483646 2147483647
# 0 1
# 0 2
# 0 3
# 0 4
#
# 출력:
# 7
# 3
# 92681
# 92681
# 92681
# 92681
# 92680
# 3
# 3
# 2
# 1
# 1
# 2
# 3
# 3