t = int(input())

for _ in range(t):
    case = input()
    n, m = map(int, input().split())
    jun = list(map(int, input().split()))
    bi = list(map(int, input().split()))

    # while True:
    #     if min(jun) >= min(bi):
    #         bi.pop(bi.index(min(bi)))
    #     else:
    #         jun.pop(jun.index(min(jun)))
    #
    #     if not jun or not bi:
    #         break
    #
    # if not jun:
    #     print('B')
    # else:
    #     print('S')

    if max(jun) >= max(bi):
        print('S')
    else:
        print('B')