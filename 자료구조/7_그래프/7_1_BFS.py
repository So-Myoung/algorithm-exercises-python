
# 백준 - 바이러스
# BFS, 큐 사용, 2차원 배열 사용

from collections import deque

n = int(input())
v = int(input())
graph = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for _ in range(v):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


def bfs(node):
    queue = deque([node])
    visited[node] = True
    cnt = 0

    while queue:
        v = queue.popleft()
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                cnt += 1
    return cnt


print(bfs(1))

# 테스트 케이스
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7