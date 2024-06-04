
# 프로그래머스 알고리즘 고득점 kit
# 그리드 - 조이스틱 : Level 2

def solution(name):
    change_move = 0
    cursor_move = len(name) - 1

    for i, s in enumerate(name):
        # 알파벳 변경 이동(상하) 최소값 찾기
        change_move += min(ord(s) - ord('A'), ord('Z') - ord(s) + 1)

        # 커서 이동(좌우)의 최소값을 찾기 위한 연속된 A 문자열 찾기, next는 마지막 A 다음 index
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 커서 이동(좌우) 최소값 갱신
        cursor_move = min([cursor_move, 2 * i + (len(name) - next), 2 * (len(name) - next) + i])

    return change_move + cursor_move


def main():
    n = input()
    print(solution(n))


if __name__ == "__main__":
    main()