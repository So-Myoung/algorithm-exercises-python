# 프로그래머스 - 게임 맵 최단거리

# 7-3. 미로탈출과 거의 똑같은 문제
# 불필요한 코드 줄이고 조금 더 깔끔하게 작성하기 연습

from collections import deque


def solution(maps):
    dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    n, m = len(maps), len(maps[0])
    queue = deque([(0, 0)])

    while queue:
        x, y = queue.popleft()

        # 도착 지점의 거리가 업데이트 되면 더 이상 업데이트 되지 않고,
        # 이 시점이 최단 거리기 때문에, return 하면 불필요한 반복을 줄일 수 있음
        if x == n - 1 and y == m - 1:
            return maps[x][y]

        for dx, dy in dir:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))

    return -1


def main():
    # 테스트 케이스 1
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 1], [0, 0, 0, 0, 1]]))
    # 테스트 케이스 2
    print(solution([[1, 0, 1, 1, 1], [1, 0, 1, 0, 1], [1, 0, 1, 1, 1], [1, 1, 1, 0, 0], [0, 0, 0, 0, 1]]))


if __name__ == "__main__":
    main()


# return을 다르게 하는 방식

# def solution(maps):
#     dir = [(-1, 0), (1, 0), (0, -1), (0, 1)]
#     n, m = len(maps), len(maps[0])
#     queue = deque([(0, 0)])
#
#     while queue:
#         x, y = queue.popleft()
#
#         for dx, dy in dir:
#             nx, ny = x + dx, y + dy
#
#             if 0 <= nx < n and 0 <= ny < m and maps[nx][ny] == 1:
#                 maps[nx][ny] = maps[x][y] + 1
#                 queue.append((nx, ny))
#
#     answer = maps[n - 1][m - 1]
#     return -1 if answer == 1 else answer
