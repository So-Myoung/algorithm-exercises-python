
# 삽입 정렬 구현

def solution(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break

    return array


def main():
    # 테스트 케이스 1
    print(solution([7, 5, 9, 0, 3, 1, 6, 2, 4, 8]))
    # 테스트 케이스 2
    print(solution([1, 5, 2, 6, 3, 7, 4]))


if __name__ == "__main__":
    main()
