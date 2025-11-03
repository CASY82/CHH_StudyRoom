import sys
import math
from itertools import combinations

input = sys.stdin.readline

def solve():
    T = int(input().strip())
    out_lines = []
    for _ in range(T):
        n = int(input().strip())
        pts = [tuple(map(int, input().split())) for _ in range(n)]
        total_x = sum(x for x, _ in pts)
        total_y = sum(y for _, y in pts)

        half = n // 2
        # 조합으로 시작점(+1)으로 쓸 half개를 고른다
        best = float('inf')

        # 미세 최적화: x, y 따로 리스트로 빼두기
        xs = [p[0] for p in pts]
        ys = [p[1] for p in pts]

        # 조합을 전부 순회
        for comb in combinations(range(n), half):
            sx = sum(xs[i] for i in comb)
            sy = sum(ys[i] for i in comb)
            vx = 2 * sx - total_x
            vy = 2 * sy - total_y
            val = math.hypot(vx, vy)
            if val < best:
                best = val

        out_lines.append(f"{best:.12f}")

    print("\n".join(out_lines))

if __name__ == "__main__":
    solve()