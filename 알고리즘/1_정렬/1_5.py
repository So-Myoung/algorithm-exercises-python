
# 정렬 - 정수 내림차순으로 배치하기

def solution(n):
    return int("".join(sorted(str(n), reverse=True)))


def main():
    # 테스트 케이스 1
    print(solution(118372))


if __name__ == "__main__":
    main()
