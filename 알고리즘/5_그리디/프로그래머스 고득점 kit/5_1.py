
# 프로그래머스 알고리즘 고득점 kit
# 그리드 - 체육복 : Level 1

def solution(n, lost, reserve):
    new_reserve = set(reserve) - set(lost)
    new_lost = set(lost) - set(reserve)

    for r in new_reserve:
        if r - 1 in new_lost:
            new_lost.remove(r - 1)
        elif r + 1 in new_lost:
            new_lost.remove(r + 1)

    return n - len(new_lost)


def main():
    n = int(input())
    lost = list(map(int, input().split()))
    reserve = list(map(int, input().split()))

    print(solution(n, lost, reserve))


if __name__ == "__main__":
    main()