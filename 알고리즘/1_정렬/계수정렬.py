# 계수 정렬 구현

def solution(array):
    count = [0] * (max(array) + 1)
    res = []

    for i in range(len(array)):
        count[array[i]] += 1

    for i in range(len(count)):
        for j in range(count[i]):
            res.append(i)

    return res


def main():
    # 테스트 케이스 1
    print(solution([7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]))


if __name__ == "__main__":
    main()
