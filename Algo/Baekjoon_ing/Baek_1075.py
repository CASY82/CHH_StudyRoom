n = int(input())
f = int(input())
result = 0

val = (n // 100) * 100
middle_val = (val // f)

if (val % f) == 0:
    result_val = middle_val * f
else:
    result_val = (middle_val + 1) * f

result = (result_val % 100)

print('%02d' %result)

