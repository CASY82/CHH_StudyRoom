import sys

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()

table = [[""] * (len(second)+1) for _ in range((len(first)+1))]

#LCS1 문제는 길이만 구하는 문제였다.
#해당 길이를 셀 때 추가하는 문자가 동일하므로 해당 로직을 찾아서 다음과 같이 변형
def lcs(m, n):
    for i in range(1, m+1):
        for j in range(1, n+1):
            if first[i-1] == second[j-1]:
                #문자를 추가하는 방식으로 변경
                table[i][j] = table[i-1][j-1] + first[i-1]
            else:
                # 기존에는 수를 넣는거라 max 사용이 되었으나 문자로 바뀌면서 변형을 줘야 함
                if len(table[i-1][j]) > len(table[i][j-1]):
                    table[i][j] = table[i-1][j]
                else:
                    table[i][j] = table[i][j-1]

    return table[m][n]

result = lcs(len(first), len(second))
print(len(result), result, sep = "\n")