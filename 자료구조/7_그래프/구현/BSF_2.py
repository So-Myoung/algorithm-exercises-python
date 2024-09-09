# 그래프 - 넓이 우선 탐색(BFS)
# defaultdict 이용 구현

from collections import defaultdict, deque


def solution(graph, start):
    res = []
    visited = set()

    adj_list = defaultdict(list)
    for s, v in graph:
        adj_list[s].append(v)

    # BFS 탐색
    def bfs(start):
        # 맨 처음 방문 노드 푸시 및 방문 처리
        queue = deque([start])
        visited.add(start)
        res.append(start)

        while queue:
            node = queue.popleft()
            for n in adj_list.get(node, []):  # 인접 노드 호출
                if n not in visited:
                    # 방문 이력 없는 인접 노드 방문 처리
                    queue.append(n)
                    visited.add(n)
                    res.append(n)

    bfs(start)
    return res


def main():
    # 테스트 케이스 1
    print(solution([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 8), (6, 9), (7, 9)], 1))
    # 테스트 케이스 2
    print(solution([(0, 1), (1, 2), (2, 3), (3, 4), (4, 5), (5, 0)], 1))


if __name__ == "__main__":
    main()
