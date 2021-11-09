n, b = input().split()
alpha_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
sum = 0
n = n[::-1]
b = int(b)

for i in range(len(n)):
    if n[i] in alpha_list:
        sum += ((alpha_list.index(n[i]) + 10) * (b ** i))
    else:
        sum += (int(n[i]) * (b ** i))

print(sum)

#파이써닉한 방법으로는 다음과 같다.
# a,b = input().split()
# print(int(a,int(b)))