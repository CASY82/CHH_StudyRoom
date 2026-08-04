# 치킨 쿠폰
def solution(chicken):
    answer = 0
    coupon = chicken

    while coupon >= 10:
        tmp = coupon // 10
        tmp2 = coupon % 10
        answer += tmp
        coupon = tmp + tmp2

    return answer

print(solution(100))
print(solution(1081))
