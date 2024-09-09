
# 백준 - 바이러스
# DFS, 재귀함수 사용, 2차원 배열 사용

n = int(input())
v = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def dfs(node, cnt):
    visited[node] = True
    for n in graph[node]:
        if not visited[n]:
            cnt = dfs(n, cnt + 1)
    return cnt


print(dfs(1, 0))
