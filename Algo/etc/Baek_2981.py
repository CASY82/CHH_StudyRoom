import sys

diff_num_list = []
num_list = []
result = []

def Euclid(a, b):
    if a % b == 0:
        return b
    else:
        return Euclid(b, a%b)

n = int(sys.stdin.readline())

for _ in range(n):
    num_list.append(int(sys.stdin.readline()))

# A = a * x + l / B = b * x + l ==> A-B = x(a-b)
# 먼저 두 수의 차를 구한다.
for i in range(1, len(num_list)):
    diff_num_list.append(abs(num_list[i] - num_list[i - 1]))

# 차이의 집합들의 공약수를 구한다.
while len(diff_num_list) != 1:
    for j in range(1, len(diff_num_list)):
        diff_num_list[j - 1] = Euclid(diff_num_list[j], diff_num_list[j - 1])

    diff_num_list.pop()

tmp = diff_num_list[0]
result = set()

# 구한 공약수의 약수들을 구하면 됨
for yaksu in range(1, int(tmp ** 0.5) + 1):
    if tmp % yaksu == 0:
        result.add(yaksu)
        result.add(tmp//yaksu)

result = list(result)
result.sort()
result.pop(0)
print(*result)