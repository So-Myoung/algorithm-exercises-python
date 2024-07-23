# 프로그래머스 알고리즘 고득점 kit
# 구현(완전탐색) - 카펫

def solution(brown, yellow):
    answer = []

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            yellow_x = yellow // i
            yellow_y = i
            if 2 * yellow_x + 2 * yellow_y + 4 == brown:
                answer.append(yellow_x + 2)
                answer.append(yellow_y + 2)
                break

    return sorted(answer, reverse=True)


def main():
    # 테스트 케이스 1
    print(solution(10, 2))
    # 테스트 케이스 2
    print(solution(8, 1))
    # 테스트 케이스 3
    print(solution(24, 24))


if __name__ == "__main__":
    main()
