# 해시 - 메뉴 리뉴얼
# 2021 KAKAO BLIND RECRUITMENT

from itertools import combinations
from collections import Counter


def solution(orders, course):
    res = []

    for c in course:
        menu = []

        for order in orders:
            menu += combinations(sorted(order), c)

        counter = Counter(menu)

        # 최소 2명 이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스 요리 메뉴 후보에 포함
        if counter and max(counter.values()) > 1:
            for menu, cnt in counter.items():
                if cnt == max(counter.values()):
                    res.append(''.join(menu))

    return sorted(res)


def main():
    # 테스트 케이스 1
    print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
    # 테스트 케이스 2
    print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]))
    # 테스트 케이스 3
    print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))


if __name__ == "__main__":
    main()
