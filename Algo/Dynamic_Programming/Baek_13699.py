import sys

#메모이제이션이 없으면 아마도 시간초과

n = int(sys.stdin.readline())
t_arr = [1] + [0 for _ in range(35)]

def func(n):
    if n == 0:
        return t_arr[0]
    elif t_arr[n] > 0:
        return t_arr[n]
    else:
        for i in range(n):
            t_arr[n] += func(i) * func(n - 1 - i)

        return t_arr[n]

func(n)
print(t_arr[n])