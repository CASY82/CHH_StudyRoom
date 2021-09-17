#요약하자면 주사위에서 나온 숫자들 중 만들 수 있는 수 중 제일 작은 수

dice = [[1, 6, 2, 5, 3, 4], [9, 9, 1, 0, 7, 8]]

def solution(dice):
    dice.sort(key=lambda x:x[0])
    dice_result = []
    result = 10

    for i in range(len(dice)):
        dice[i].sort()

    for i in range(len(dice)):
        for j in range(len(dice)):
            for k in range(6):
                for z in range(6):
                    if i != j:
                        dice_result.append(int(str(dice[i][k]) + str(dice[j][z])))

    dice_result.sort()

    # for i in dice_result:
    #     if result == i:
    #         result += 1
    #     else:



    print(dice)
    print(dice_result)






print(solution(dice))