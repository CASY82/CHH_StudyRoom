import sys

t = int(sys.stdin.readline())

for _ in range(t):
    hp, mp, atk, defen, hp_af, mp_af, atk_af, defen_af = map(int, sys.stdin.readline().split())

    if hp + hp_af < 1:
        result_hp = 1
    else:
        result_hp = hp + hp_af

    if mp + mp_af < 1:
        result_mp = 1
    else:
        result_mp = mp + mp_af

    if atk + atk_af < 0:
        result_atk = 0
    else:
        result_atk = atk + atk_af

    result_defen = defen + defen_af

    print(result_hp + result_mp * 5 + 2 * result_atk + 2 * result_defen)