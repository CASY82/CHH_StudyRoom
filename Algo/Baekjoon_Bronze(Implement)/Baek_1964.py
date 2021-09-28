n = int(input())
result = 5

for i in range(2, n + 1):
    result += (3 * i + 1)

print(result % 45678)

#좀더 짧은 점화식
# a=int(input())
# print((((3*a*a+5*a)//2)+1)%45678)