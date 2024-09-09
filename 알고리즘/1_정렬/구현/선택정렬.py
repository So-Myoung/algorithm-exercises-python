
# 선택 정렬 구현

def solution(array):
    for i in range(len(array)):
        min_index = i
        for j in range(i + 1, len(array)):
            if array[min_index] > array[j]:
                min_index = j
        array[i], array[min_index] = array[min_index], array[i]

    return array


def main():
    # 테스트 케이스 1
    print(solution([7, 5, 9, 0, 3, 1, 6, 2, 4, 8]))
    # 테스트 케이스 2
    print(solution([1, 5, 2, 6, 3, 7, 4]))


if __name__ == "__main__":
    main()
