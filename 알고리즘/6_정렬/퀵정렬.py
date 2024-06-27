# 퀵 정렬 구현

def quick_sort(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x <= pivot]
    right_side = [x for x in tail if x > pivot]

    return quick_sort(left_side) + [pivot] + quick_sort(right_side)


def main():
    # 테스트 케이스 1
    print(quick_sort([5, 7, 9, 0, 3, 1, 6, 2, 4, 8]))
    # 테스트 케이스 2
    print(quick_sort([1, 5, 2, 6, 3, 7, 4]))


if __name__ == "__main__":
    main()