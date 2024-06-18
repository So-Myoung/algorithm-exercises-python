
# 프로그래머스 알고리즘 고득점 kit
# 해시 - 의상 : Level 2


def solution(clothes):
    dic = {}
    res = 1

    for name, kind in clothes:
        if kind in dic.keys():
            dic[kind] += [name]
        else:
            dic[kind] = [name]

    for v in dic.values():
        # 의상을 착용 하지 않는 경우도 존재하므로 + 1
        res *= (len(v) + 1)

    # 아무것도 착용하지 않는 경우 제외
    return res - 1


def main():
    # 테스트 케이스 1
    print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]))
    # 테스트 케이스 2
    print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]]))


if __name__ == "__main__":
    main()
