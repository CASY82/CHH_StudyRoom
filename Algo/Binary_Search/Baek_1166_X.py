import sys

n, l, w, h = map(int, sys.stdin.readline().split())
# 이 부분 처리에서 헤매는 바람에 참고하여 품
s, e = 0, max(l, w, h)

for _ in range(10000):
    # a값이라고 생각하면 될듯
    mid = (s + e) / 2
    # 각 변마다 미리 a값을 나누어 개수를 바로 구한다.
    cnt = (l // mid) * (w // mid) * (h // mid)
    # 원래 갯수보다 cnt가 많으면 큰 값이 줄어야 되므로 s, 반대는 당연히 e
    if cnt >= n:
        s = mid
    else:
        e = mid

print("%.10f" % (e))