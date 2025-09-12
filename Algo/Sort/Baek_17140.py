import sys
from collections import Counter

def read_input():
    r, c, k = map(int, sys.stdin.readline().split())
    A = [list(map(int, sys.stdin.readline().split())) for _ in range(3)]
    return r-1, c-1, k, A  # 0-index로 변환

def pad_rows(rows, max_len):
    for row in rows:
        if len(row) < max_len:
            row.extend([0] * (max_len - len(row)))
    return rows

def R_op(A):
    new_rows = []
    max_len = 0
    for row in A:
        cnt = Counter(x for x in row if x != 0)
        # (수, 등장횟수) → (등장횟수, 수) 기준으로 정렬
        pairs = sorted(cnt.items(), key=lambda x: (x[1], x[0]))
        flat = []
        for num, c in pairs:
            flat.append(num)
            flat.append(c)
        # 길이 100 초과 시 자르기
        if len(flat) > 100:
            flat = flat[:100]
        new_rows.append(flat)
        max_len = max(max_len, len(flat))
    # 가장 긴 행 길이에 맞춰 0 패딩
    new_rows = pad_rows(new_rows, max_len)
    return new_rows

def transpose(M):
    return [list(x) for x in zip(*M)] if M and M[0] else []

def C_op(A):
    # 열 기준 연산은 전치 → R_op → 전치
    T = transpose(A)
    T2 = R_op(T)
    return transpose(T2)

def solve():
    r, c, k, A = read_input()

    for t in range(101):  # 0초부터 100초까지
        # 범위 안이면 즉시 검사
        if 0 <= r < len(A) and 0 <= c < len(A[0]) and A[r][c] == k:
            print(t)
            return

        if t == 100:  # 100초까지 안되면 -1
            print(-1)
            return

        # 다음 연산 결정
        R, C = len(A), len(A[0])
        if R >= C:
            A = R_op(A)
        else:
            A = C_op(A)

        # 행/열 길이가 100을 넘을 수 있으니 한번 더 안전하게 잘라줌
        if len(A) > 100:
            A = A[:100]
        if A and len(A[0]) > 100:
            A = [row[:100] for row in A]

if __name__ == "__main__":
    solve()
