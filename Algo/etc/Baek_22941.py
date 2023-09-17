import sys

hp_hero, atk_hero, hp_mao, atk_mao = map(int, sys.stdin.readline().split())
p, s = map(int, sys.stdin.readline().split())

mao_chance = True

tmp_m = hp_mao // atk_hero
tmp_h = hp_hero // atk_mao

min_tmp = min(tmp_h, tmp_m)

hp_mao -= (min_tmp-2) * atk_hero
hp_hero -= (min_tmp-2) * atk_mao

while True:

    hp_mao -= atk_hero

    if hp_mao <= 0:
        print("Victory!")
        break

    hp_hero -= atk_mao

    if hp_hero <= 0:
        print("gg")
        break

    if 1 <= hp_mao <= p:
        if mao_chance:
            hp_mao += s

            tmp_m = hp_mao // atk_hero
            tmp_h = hp_hero // atk_mao

            min_tmp = min(tmp_h, tmp_m)

            hp_mao -= (min_tmp - 2) * atk_hero
            hp_hero -= (min_tmp - 2) * atk_mao

            mao_chance = False


# 다른 사람 풀이
# import sys
# input = sys.stdin.readline
#
# HP, ATK, HP_Boss, ATK_Boss = map(int, input().split())
#
# P, S = map(int, input().split())
#
# turn1 = HP // ATK_Boss
# if HP % ATK_Boss:
#     turn1 += 1
#
# if (HP_Boss - P) % ATK and (HP_Boss - P) % ATK + P <= ATK:
#     turn2 = HP_Boss // ATK
#     if HP_Boss % ATK:
#         turn2 += 1
#
# else:
#     turn2 = (HP_Boss + S) // ATK
#     if (HP_Boss + S) % ATK:
#         turn2 += 1
#
# if turn1 >= turn2:
#     print('Victory!')
# else:
#     print('gg')

# 다른 사람 풀이 2

# import sys
# input = sys.stdin.readline
#
# HP, ATK, HP_Boss, ATK_Boss = map(int, input().split())
#
# P, S = map(int, input().split())
#
# turn1 = HP // ATK_Boss
# if HP % ATK_Boss:
#     turn1 += 1
#
# if (HP_Boss - P) % ATK and (HP_Boss - P) % ATK + P <= ATK:
#     turn2 = HP_Boss // ATK
#     if HP_Boss % ATK:
#         turn2 += 1
#
# else:
#     turn2 = (HP_Boss + S) // ATK
#     if (HP_Boss + S) % ATK:
#         turn2 += 1
#
# if turn1 >= turn2:
#     print('Victory!')
# else:
#     print('gg')
