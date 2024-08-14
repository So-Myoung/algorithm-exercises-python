
# 트리 - 예상 대진표

def solution(n, a, b):
    answer = 0
    while a != b:
        a = (a + 1) // 2
        b = (b + 1) // 2
        answer += 1

    return answer


def main():
    # 테스트 케이스 1
    print(solution(8, 4, 7))


if __name__ == "__main__":
    main()