# 그래프 - 깊이 우선 탐색(DFS) 심화

# defaultdict 란? dictionary 의 모든 키에 default 값을 설정
# defaultdict(int) -> 0
# defaultdict(str) -> ""
# defaultdict(list) -> []

from collections import defaultdict


def solution(graph, start):
    res = []
    visited = set()  # 각 노드의 방문 여부 리스트

    # 인접 리스트 형태로 변경
    adj_list = defaultdict(list)
    for s, v in graph:
        adj_list[s].append(v)
        # ex) defaultdict(<class 'list'>, {'A': ['B', 'C'], 'B': ['D', 'E'], 'C': ['F'], 'E': ['F']})

    # DFS 탐색(재귀 함수)
    def dfs(node, visited, res):
        visited.add(node)  # 방문 여부 -> 집합 -> add
        res.append(node)  # 결과 -> 리스트 -> append

        for n in adj_list.get(node, []):  # dictionary get 함수 -> get(key 값, default 값)
            if n not in visited:
                dfs(n, visited, res)  # 재귀 호출

    dfs(start, visited, res)
    return res


def main():
    # 테스트 케이스 1
    print(solution([['A', 'B'], ['B', 'C'], ['C', 'D'], ['D', 'E']], 'A'))
    # 테스트 케이스 2
    print(solution([['A', 'B'], ['A', 'C'], ['B', 'D'], ['B', 'E'], ['C', 'F'], ['E', 'F']], 'A'))

    # -> input 값을 인접 리스트 형태로 변환하는 과정이 필요


if __name__ == "__main__":
    main()
