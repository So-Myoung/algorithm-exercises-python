# 구현 - 왕실의 나이트

def solution(s):
    res = 0
    x = int(ord(s[0])) - int(ord('a')) + 1
    y = int(s[1])

    move_types = [(-1, 2), (1, 2), (2, 1), (2, -1), (-1, -2), (1, -2), (-2, 1), (2, -1)]

    for move in move_types:
        nx = x + move[0]
        ny = y + move[1]
        if (1 <= nx <= 8) and (1 <= ny <= 8):
            res += 1

    return res


def main():
    # 테스트 케이스 1
    print(solution('a1'))
    # 테스트 케이스 2
    print(solution('c2'))


if __name__ == "__main__":
    main()
