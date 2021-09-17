n = int(input())

for i in range(n*2-1):
    for j in range(1, n*2):
        if i < n:
           if n + i >= j and n - i <= j:
               print('*', end='')
           elif n - i > j:
               print(' ', end='')
        else:
            if n + (n * 2 - 2 - i) >= j and n - (n * 2 - 2 - i) <= j:
                print('*', end='')
            elif n - (n * 2 - 2 - i) > j:
                print(' ', end='')

    print()


#뭔가 너무 복잡하게 푼거 같다. 단순하게 푼 예시
# n=int(input())
#
# for i in range(1,n+1):
#   print(" "*(n-i)+"*"*(1+2*(i-1)))
#
#
# for i in range(2,n+1):
#   print(" "*(i-1)+"*"*(1+(n-i)*2))
