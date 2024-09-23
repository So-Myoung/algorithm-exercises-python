# 프로그래머스 알고리즘 고득점 kit
# 구현(완전탐색) - 전력망을 둘로 나누기

# visited(방문 여부) 사용하는 방식


def dfs(node, graph, visited):
    cnt = 1
    visited[node] = True

    for connected in graph[node]:
        if not visited[connected]:
            cnt += dfs(connected, graph, visited)

    return cnt


def solution(n, wires):
    graph = [[] for _ in range(n + 1)]

    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)

    min_diff = float("inf")

    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        visited = [False] * (n + 1)

        cnt_a = dfs(a, graph, visited)
        cnt_b = n - cnt_a

        # 두 전력망이 가지고 있는 송전탑 개수의 차이(절대값)를 return
        min_diff = min(min_diff, abs(cnt_a - cnt_b))

        graph[a].append(b)
        graph[b].append(a)

    return min_diff


def main():
    # 테스트 케이스 1
    print(solution(9, [[1, 3], [2, 3], [3, 4], [4, 5], [4, 6], [4, 7], [7, 8], [7, 9]]))

    # 테스트 케이스 2
    print(solution(4, [[1, 2], [2, 3], [3, 4]]))

    # 테스트 케이스 3
    print(solution(7, [[1, 2], [2, 7], [3, 7], [3, 4], [4, 5], [6, 7]]))


if __name__ == "__main__":
    main()
