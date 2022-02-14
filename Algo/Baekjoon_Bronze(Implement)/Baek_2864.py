a, b = input().split()

#최솟값 모든 6을 5로
minimum = 0

min_a = a.replace('6', '5')
min_b = b.replace('6', '5')

minimum = int(min_a) + int(min_b)

#최댓값 모든 5를 6으로
maximum = 0

max_a = a.replace('5', '6')
max_b = b.replace('5', '6')

maximum = int(max_a) + int(max_b)

print(minimum, maximum)