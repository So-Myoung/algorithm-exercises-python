
# 프로그래머스 알고리즘 고득점 kit
# 정렬 - H-Index

def solution(citations):
    citations.sort(reverse=True)

    for i, h in enumerate(citations):
        if i >= h:
            return i

    return len(citations)


def main():
    # 테스트 케이스 1
    print(solution([3, 0, 6, 1, 5]))
    # 테스트 케이스 2
    print(solution([5, 5, 5, 5]))


if __name__ == "__main__":
    main()
