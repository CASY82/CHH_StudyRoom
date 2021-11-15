angle = []

for _ in range(3):
    angle.append(int(input()))

if sum(angle) == 180:
    if len(set(angle)) == 2:
        print("Isosceles")
    elif len(set(angle)) == 3:
        print("Scalene")
    else:
        print("Equilateral")
else:
    print("Error")