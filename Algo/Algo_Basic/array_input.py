#2차원 배열 입력 받기

# 1. arr[i] 하나씩 입력 받기
# for i in range(B):
# 	arr[i] = list(map(int, input().split()))

# 2. arr 한 list씩 append
# for i in range(B):
# 	arr.append(list(map(int, input().split())))

# 3. 선언과 동시에 입력 받기
# arr = [list(map(int, input().split())) for _ in range(B)]

# 띄어쓰기 없이 입력 받는 경우 .split()제거
# chess_board = [list(map(str, input())) for _ in range(8)]
