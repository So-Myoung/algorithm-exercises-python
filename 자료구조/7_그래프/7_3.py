# 그래프 - 넓이 우선 탐색(BFS)


from collections import deque


def solution(graph):
    def bfs(graph, start, visited):
        queue = deque([start])
        visited[start] = True

        while queue:
            v = queue.popleft()
            print(v, end=' ')
            for i in graph[v]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    visited = [False] * len(graph)
    bfs(graph, 1, visited)


def main():
    # 테스트 케이스 1
    # input 값 = 인접 리스트 형태
    solution([[],  # index 0
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
