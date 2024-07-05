# 프로그래머스 알고리즘 고득점 kit
# 정렬 - H-Index

def solution(citations):
    h_index = 0
    citations.sort(reverse=True)

    for i, h in enumerate(citations):  # 테스트 케이스 1 -> [(0, 6), (1, 5), (2, 3), (3, 1), (4, 0)]
        if h >= i + 1:
            h_index = i + 1

    return h_index


def main():
    # 테스트 케이스 1
    print(solution([3, 0, 6, 1, 5]))
    # # 테스트 케이스 2
    print(solution([5, 5, 5, 5]))
    # 테스트 케이스 3
    print(solution([9, 8, 7, 2, 2]))


if __name__ == "__main__":
    main()
