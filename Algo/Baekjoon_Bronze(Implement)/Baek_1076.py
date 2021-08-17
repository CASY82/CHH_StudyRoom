#이제보니 중간의 color_value는 없어도 된다. fc = color.index(input())을 이용하면 한번에 된다

color = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
color_value = [i for i in range(10)]
color_mul = [10 ** i for i in range(10)]
result = 0

fc = input()
sc = input()
tc = input()

result += int(str(color_value[color.index(fc)]) + str(color_value[color.index(sc)])) * color_mul[color.index(tc)]

print(result)
