#2번 부터 하자

n = int(input())
del_num = []


def solution(n):
    result = 0

    if n > 0:
        n_list = list(map(int, str(n)))

        for i in range(len(n_list)):
            if int(n_list[i]) == 5:
                if int(n_list[i]) < int(n_list[i + 1]):
                    del_num.append(i)
                else:
                    if not del_num:
                        del_num.append(i)
                    else:
                        continue

        del n_list[del_num[0]]

        for i in range(len(n_list)):
            result += n_list[i] * (10 ** (len(n_list) - i - 1))

        return result

    else:
        n= -n
        n_list = list(map(int, str(n)))

        for i in range(len(n_list)):
            if int(n_list[i]) == 5:
                if int(n_list[i]) > int(n_list[i + 1]):
                    del_num.append(i)
                else:
                    continue
        del_num.sort(reverse=True)
        del n_list[del_num[0]]
        print(n_list)

        for i in range(len(n_list)):
            result += n_list[i] * (10 ** (len(n_list) - i - 1))

        return result

print(solution(n))
