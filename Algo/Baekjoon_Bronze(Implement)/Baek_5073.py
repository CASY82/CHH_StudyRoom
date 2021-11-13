while True:
    triangle = list(map(int, input().split()))
    if sum(triangle) == 0:
        break

    triangle.sort()

    if triangle[0] + triangle[1] > triangle[2]:
        if len(set(triangle)) == 1:
            print('Equilateral')
        elif len(set(triangle)) == 2:
            print('Isosceles')
        else:
            print('Scalene')
    else:
        print('Invalid')