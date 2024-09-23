# 구현 (시뮬레이션) - 두 행렬을 곱한 후 전치 행렬 만들기


def multi(matrix1, matrix2):
    res = [[0 for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            for k in range(3):
                res[i][j] += matrix1[i][k] * matrix2[k][j]

    return res


def trans(matrix):
    res = [[0 for _ in range(3)] for _ in range(3)]

    for i in range(3):
        for j in range(3):
            res[j][i] = matrix[i][j]

    return res


def solution(matrix1, matrix2):
    multi_matrix = multi(matrix1, matrix2)
    trans_matrix = trans(multi_matrix)

    return trans_matrix


def main():
    # 테스트 케이스 1
    print(solution(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ],
        [
            [9, 8, 7],
            [6, 5, 4],
            [3, 2, 1]
        ]
    ))

    # 테스트 케이스 2
    print(solution(
        [
            [2, 4, 6],
            [1, 3, 5],
            [7, 8, 9]
        ],
        [
            [9, 1, 2],
            [4, 5, 6],
            [7, 3, 8]
        ]
    ))


if __name__ == "__main__":
    main()