# 구현 (시뮬레이션) - 배열 회전하기


def rotate(arr):
    n = len(arr)  # 문제 조건 : 2차원 배열의 행과 열의 크기는 같음

    rotate_arr = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotate_arr[j][n - 1 - i] = arr[i][j]

    return rotate_arr


def solution(arr, n):
    answer = arr.copy()

    for _ in range(n):
        answer = rotate(answer)

    return answer


def main():
    # 테스트 케이스 1
    print(solution([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ], 1))
    # 테스트 케이스 2
    print(solution([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ], 2))


if __name__ == "__main__":
    main()
