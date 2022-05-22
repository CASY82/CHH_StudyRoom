import sys
sys.setrecursionlimit(30000)

depth = int(sys.stdin.readline())
visitied = list(map(int, sys.stdin.readline().split()))
tree = [[] for _ in range(depth)]

def TreeSearch(arr, now_depth):
    # 가운데 중심 노드
    mid = (len(arr) // 2)
    tree[now_depth].append(arr[mid])

    # 가운데를 중심으로 배열을 반반 나누게 되는데, 이 때 1개일 경우 마지막 리프 노드이므로 리턴~!
    if len(arr) == 1:
        return

    # 미드 값을 중심으로 양 사이드 노드 배열을 갈라서 재귀 한다.
    TreeSearch(arr[:mid], now_depth + 1)
    TreeSearch(arr[mid+1:], now_depth + 1)

TreeSearch(visitied, 0)
for i in range(depth):
    print(*tree[i])