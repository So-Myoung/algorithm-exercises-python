# 배열 - 방문 길이
# Summer/Winter Coding(~2018)

def is_valid_move(nx, ny):
    return -5 <= nx <= 5 and -5 <= ny <= 5


def move(x, y, dir):
    if dir == 'U':
        nx, ny = x, y + 1
    elif dir == 'D':
        nx, ny = x, y - 1
    elif dir == 'L':
        nx, ny = x - 1, y
    elif dir == 'R':
        nx, ny = x + 1, y
    return nx, ny


def solution(dirs):
    res = set()
    x, y = 0, 0

    for dir in dirs:
        nx, ny = move(x, y, dir)
        if not is_valid_move(nx, ny):
            continue
        res.add((x, y, nx, ny))
        res.add((nx, ny, x, y))
        x, y = nx, ny  # 옮긴 좌표로 업데이트

    return int(len(res) / 2)


def main():
    # 테스트 케이스 1
    print(solution("ULURRDLLU"))
    # 테스트 케이스 2
    print(solution("LULLLLLLU"))


if __name__ == "__main__":
    main()
