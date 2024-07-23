# 구현 - 시각

def solution(hour, k):
    answer = 0

    for h in range(hour + 1):
        for m in range(60):
            for s in range(60):
                if str(k) in f'{h:02d}:{m:02d}:{s:02d}':  # k = 0일 경우 고려
                    answer += 1

    return answer


def main():
    # 테스트 케이스 1
    print(solution(5, 3))
    # 테스트 케이스 2
    print(solution(5, 0))


if __name__ == "__main__":
    main()
