# 이코테 - 미로 탈출

from collections import deque

n, m = map(int, input().split())
map = [list(map(int, input())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위 벗어날 시 다음 반복으로 넘어감
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue

            # 괴물이 있는 길은 무시
            if map[nx][ny] == 0:
                continue

            # 괴물이 없고, 방문한 적 없는 곳만 방문
            if map[nx][ny] == 1:
                map[nx][ny] = map[x][y] + 1
                queue.append((nx, ny))

    return map[n - 1][m - 1]


print(bfs(0, 0))
# print(map)
