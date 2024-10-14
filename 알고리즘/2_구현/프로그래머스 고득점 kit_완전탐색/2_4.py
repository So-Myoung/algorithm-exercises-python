# 프로그래머스 알고리즘 고득점 kit
# 구현(완전탐색) - 피로도
# 백트래킹, dfs

def dfs(k, dungeons, cnt, visited):
    answer_max = cnt

    for i in range(len(dungeons)):
        if k >= dungeons[i][0] and visited[i] == 0:
            visited[i] = 1
            answer_max = max(answer_max, dfs(k - dungeons[i][1], dungeons, cnt + 1, visited))
            visited[i] = 0

    return answer_max


def solution(k, dungeons):
    visited = [0] * len(dungeons)
    return dfs(k, dungeons, 0, visited)


def main():
    # 테스트 케이스 1
    print(solution(80, [[80, 20], [50, 40], [30, 10]]))


if __name__ == "__main__":
    main()