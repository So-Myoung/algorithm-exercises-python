# 이코테 - 음료수 얼려먹기(DFS)

n, m = map(int, input().split())
graph = []

for i in range(n):
    graph.append(list(map(int, input())))


def dfs(x, y):
    # 주어진 범위 (얼음판)을 벗어나는 경우 종료
    if x < 0 or x >= n or y < 0 or y >= m:
        return False

    # 방문 하지 않은 경우 방문 표시
    if graph[x][y] == 0:
        graph[x][y] = 1
        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j):
            result += 1

print(result)


# 입력 예시
# 4 5
# 00110
# 00011
# 11111
# 00000

# 출력 예시
# 3