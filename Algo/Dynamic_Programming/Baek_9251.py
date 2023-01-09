import sys

first = sys.stdin.readline().strip()
second = sys.stdin.readline().strip()

tmp = [[0] * (len(second)+1) for _ in range(len(first)+1)]

def lcs(first_len, second_len):
    for i in range(1, first_len+1):
        for j in range(1, second_len+1):
            if first[i-1] == second[j-1]:
                tmp[i][j] = tmp[i-1][j-1] + 1
            else:
                tmp[i][j] = max(tmp[i][j-1], tmp[i-1][j])

    return tmp[first_len][second_len]

print(lcs(len(first), len(second)))