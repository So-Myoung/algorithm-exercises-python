# 프로그래머스 알고리즘 고득점 kit
# 구현(완전탐색) - 최소직사각형

def solution(sizes):
    # max_list = []
    # min_list = []
    #
    # for size in sizes:
    #     max_list.append(max(size))
    #     min_list.append(min(size))
    #
    # return max(max_list) * max(min_list)

    return max([max(size) for size in sizes]) * max([min(size) for size in sizes])


def main():
    # 테스트 케이스 1
    print(solution([[60, 50], [30, 70], [60, 30], [80, 40]]))
    # 테스트 케이스 2
    print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))
    # 테스트 케이스 3
    print(solution([[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]))


if __name__ == "__main__":
    main()
