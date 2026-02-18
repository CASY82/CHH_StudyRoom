# 전화번호 수수께끼
import sys


def solve_one(S: str) -> str:
    cnt = [0] * 26
    for ch in S:
        cnt[ord(ch) - 65] += 1

    order = [
            (0, 'Z', "ZERO"),
            (2, 'W', "TWO"),
            (4, 'U', "FOUR"),
            (6, 'X', "SIX"),
            (8, 'G', "EIGHT"),
            (3, 'H', "THREE"),
            (5, 'F', "FIVE"),
            (7, 'S', "SEVEN"),
            (1, 'O', "ONE"),
            (9, 'I', "NINE"),
    ]

    digit_cnt = [0] * 10

    for d, key, word in order:
        k = cnt[ord(key) - 65]
        digit_cnt[d] = k
        if k:
            for ch in word:
                cnt[ord(ch) - 65] -= k

    out = []
    for d in range(10):
        out.append(str(d) * digit_cnt[d])

    return "".join(out)

t = int(sys.stdin.readline())

for case in range(1, t + 1):
    s = sys.stdin.readline().strip()
    res = solve_one(s)
    print(f"Case #{case}: {res}")