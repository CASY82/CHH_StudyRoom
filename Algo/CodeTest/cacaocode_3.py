# 20210911 3

fees = [180, 5000, 10, 600]
records = ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]

def solution(fees, records):
    answer = []
    car = []
    time = []
    in_out = []

    for i in records:
        a, b, c = map(str, i.split(" "))
        car.append(b)
        time.append(a)
        in_out.append(c)

    car = list(set(car))

    print(car)
    print(time)
    print(in_out)



    return answer

print(solution(fees, records))