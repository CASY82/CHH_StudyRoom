# 20210911 5 (테케 2개 맞음 bfs 큐 구현을 안해봐서 잘 모르겠음)

# info = [0,0,1,1,1,0,1,0,1,0,1,1]
# edges = [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]

info = [0,1,0,1,1,0,1,0,0,1,0]
edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]

def bfs(info, edges, node, sheep_count, wolf_count):
    if info[node] == 0:
        sheep_count.append(1)
    else:
        wolf_count.append(1)

    for i in range(len(edges)):
        if edges[i][0] == node:
            bfs(info, edges, edges[i][1], sheep_count, wolf_count)

    return True


def solution(info, edges):
    answer = 0
    sheep_count = []
    wolf_count = []

    bfs(info, edges, edges[0][0], sheep_count, wolf_count)

    print(sheep_count)
    print(wolf_count)

    answer = sum(sheep_count)

    return answer

print(solution(info, edges))