# 구현 - 상하좌우
# 2차원 좌표 이동 x 2차원 배열 이동 o -> 문제 예제 그림 참고

def is_vaild_move(n, nx, ny):
    return 1 <= nx <= n and 1 <= ny <= n


def solution(n, plans):
    x, y = 1, 1

    for dir in plans:
        if dir == 'U':
            nx, ny = x - 1, y
        elif dir == 'D':
            nx, ny = x + 1, y
        elif dir == 'L':
            nx, ny = x, y - 1
        elif dir == 'R':
            nx, ny = x, y + 1

        if not is_vaild_move(n, nx, ny):
            continue

        x, y = nx, ny

    return [x, y]


def main():
    print(solution(5, ['R', 'R', 'R', 'U', 'D', 'D']))


if __name__ == "__main__":
    main()
