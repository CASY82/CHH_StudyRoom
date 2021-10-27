n = int(input())
a = 0
b = 1
c = 1

for i in range(1, n):
    c = a + b
    a = b
    b = c

if n == 1:
    print(1)
elif n == 2:
    print(1)
else:
    print(c)
