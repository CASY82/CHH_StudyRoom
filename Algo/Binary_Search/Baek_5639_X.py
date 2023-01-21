import sys
sys.setrecursionlimit(300000)

#이진 탐색의 기본 개념 숙지 필요할듯

nodes = []

while True:
    try:
        num = int(sys.stdin.readline())
    except:
        break

    nodes.append(num)

def postorder(first, end):
    if first > end:
        return

    #루트보다 큰 값이 없는 경우
    mid = end + 1
    for i in range(first+1, end+1):
        if nodes[first] < nodes[i]:
            mid = i
            break

    postorder(first+1, mid-1)
    postorder(mid, end)
    print(nodes[first])

postorder(0, len(nodes)-1)