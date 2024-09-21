# 그래프 - 네트워크

def dfs(computers, visited, node):
    visited[node] = True
    for i, connected in enumerate(computers[node]):
        if connected and not visited[i]:  # 노드가 연결 되어 있고, 방문 하지 않은 노드일 때
            dfs(computers, visited, i)


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for i in range(n):
        if not visited[i]:
            dfs(computers, visited, i)
            answer += 1

    return answer


def main():
    # 테스트 케이스 1
    print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
    # 테스트 케이스 2
    print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))


if __name__ == "__main__":
    main()
