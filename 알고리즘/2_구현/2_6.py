# 구현 (시뮬레이션) - 달팽이 수열 만들기
# 풀이 2

def solution(n):
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    return matrix


def main():
    # 테스트 케이스 1
    print(solution(3))

    # 테스트 케이스 2
    print(solution(4))


if __name__ == "__main__":
    main()