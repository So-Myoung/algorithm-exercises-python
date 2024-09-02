# 그래프 - 깊이 우선 탐색(DFS)


def solution(graph):
    def dfs(graph, v, visited):
        visited[v] = True
        print(v, end=' ')

        for i in graph[v]:
            if not visited[i]:
                dfs(graph, i, visited)

    visited = [False] * len(graph)  # 각 노드의 방문 여부 리스트, 인덱스와 시작 노드가 동일
    dfs(graph, 1, visited)


def main():
    # 테스트 케이스 1
    # input 값 = 인접 리스트 형태
    solution([[], # index 0
              [2, 3, 8],  # index 1
              [1, 7],  # index 2 ...
              [1, 4, 5],
              [3, 5],
              [3, 4],
              [7],
              [2, 6, 8],
              [1, 7]])


if __name__ == "__main__":
    main()
