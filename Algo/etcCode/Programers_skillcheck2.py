n = 6
arr1 = [46, 33, 33, 22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

def solution(n, arr1, arr2):
    type = [" ", "#"]
    middle = []
    sum_result = [[0 for i in range(n)] for _ in range(n)]
    result = []

    for i in range(len(arr1)):
        middle.append(arr1[i] | arr2[i])

    for i in range(len(middle)):
        imsi = str(format(middle[i], 'b')).rjust(len(middle),"0")
        for j in range(len(imsi)):
            sum_result[i][j] = type[int(imsi[j])]


    for i in range(len(sum_result)):
        result.append(''.join(sum_result[i]))

    return result

print(solution(n, arr1, arr2))