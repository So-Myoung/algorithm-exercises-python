# 구현 - 상하좌우
# 2차원 좌표 이동 x 2차원 배열 이동 o -> 문제 예제 그림 참고


def solution(n, plans):
    x, y = 1, 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    move_types = ['L', 'R', 'U', 'D']

    for plan in plans:
        for i in range(len(move_types)):
            if plan == move_types[i]:
                nx = x + dx[i]
                ny = y + dy[i]

        if nx < 1 or nx > n or ny < 1 or ny > n:
            continue

        x, y = nx, ny

    return [x, y]


def main():
    print(solution(5, ['R', 'R', 'R', 'U', 'D', 'D']))


if __name__ == "__main__":
    main()
