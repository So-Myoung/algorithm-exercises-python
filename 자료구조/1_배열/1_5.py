
# 배열 - 행렬의 곱셈
# (M * K) * (K * N) = M * N

def solution(arr1, arr2):
    r1, c1 = len(arr1), len(arr1[0])
    r2, c2 = len(arr2), len(arr2[0])

    res = [[0] * c2 for _ in range(r1)]

    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                res[i][j] += arr1[i][k] * arr2[k][j]

    return res


def main():
    # 테스트 케이스 1
    print(solution([[1, 4], [3, 2], [4, 1]], [[3, 3], [3, 3]]))
    # 테스트 케이스 2
    print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))


if __name__ == "__main__":
    main()
