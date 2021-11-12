n = int(input())

board = 2
slice = 2
count = 0

for i in range(1, n):
    board += slice
    count += 1

    if count == 2:
        slice += 1
        count = 0

print(board)

#수학 공식으로 푸는 법
# n=int(input())
# if(n%2==0):
#     x=n/2+1
#     y=n/2+1
# else:
#     x=int(n/2)+1
#     y=x+1
# print(int(x*y))