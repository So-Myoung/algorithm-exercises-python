
# 배열 - 실패율
# 2019 KAKAO BLIND RECRUITMENT

def solution(N, stages):
    challenger = [0] * (N + 2)
    fails = {}
    total = len(stages)

    for stage in stages:
        challenger[stage] += 1

    for i in range(1, N + 1):
        if challenger[i] == 0:
            fails[i] = 0
        else:
            fails[i] = challenger[i] / total
            total -= challenger[i]

    return sorted(fails, key=lambda x: fails[x], reverse=True)


def main():
    # 테스트 케이스 1
    print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
    # 테스트 케이스 2
    print(solution(4, [4, 4, 4, 4, 4]))


if __name__ == "__main__":
    main()
