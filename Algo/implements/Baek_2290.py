# LCD Test

import sys

s, n = sys.stdin.readline().split()

s = int(s)
digits = n.strip()

#
# aaaa
#f    b
#f    b
# gggg
#e    c
#e    c
# dddd
#

SEG = {
    '0': set(['a','b','c','d','e','f']),
    '1': set(['b','c']),
    '2': set(['a','b','g','e','d']),
    '3': set(['a','b','g','c','d']),
    '4': set(['f','g','b','c']),
    '5': set(['a','f','g','c','d']),
    '6': set(['a','f','g','e','c','d']),
    '7': set(['a','b','c']),
    '8': set(['a','b','c','d','e','f','g']),
    '9': set(['a','f','g','b','c','d']),
}

H_ON = " " + "-" * s + " "
H_OFF = " " + " " * s + " "

def v_line(left_on: bool, right_on: bool) -> str:
    left = "|" if left_on else " "
    right = "|" if right_on else " "
    return left + " "*s + right

rows = 2 * s + 3
out_lines = []

for r in range(rows):
    parts = []
    for ch in digits:
        seg = SEG[ch]

        if r == 0:
            parts.append(H_ON if 'a' in seg else H_OFF)
        elif 1 <= r <= s:
            parts.append(v_line('f' in seg, 'b' in seg))
        elif r == s + 1:
            parts.append(H_ON if 'g' in seg else H_OFF)
        elif s + 2 <= r <= 2 * s + 1:
            parts.append(v_line('e' in seg, 'c' in seg))
        else: #r == 2 * s + 2
            parts.append(H_ON if 'd' in seg else H_OFF)

    out_lines.append(" ".join(parts))

print("\n".join(out_lines))