seven_value, seven_gram = map(int, input().split())
other = int(input())
result = []

result.append((1000/seven_gram) * seven_value)

for i in range(other):
    other_val, other_gram = map(int, input().split())

    result.append((1000 / other_gram) * other_val)

print("{:.2f}".format(min(result)))