
# 해시 - 할인 행사

# discount 의미 = 하루에 1가지 제품만 할인, 할인 제품은 하루에 하나만 구매 가능

def solution(want, number, discount):
    want_dic = {}
    res = 0

    for i in range(len(want)):
        want_dic[want[i]] = number[i]

    for i in range(len(discount) - 9):
        discount_item = {}

        for j in range(i, i + 10):
            if discount[j] in want_dic:
                discount_item[discount[j]] = discount_item.get(discount[j], 0) + 1

        if discount_item == want_dic:
            res += 1

    return res

def main():
    # 테스트 케이스 1
    print(solution(["banana", "apple", "rice", "pork", "pot"], [3, 2, 2, 2, 1],
                   ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot",
                    "banana", "apple", "banana"]))
    # 테스트 케이스 2
    print(solution(["apple"], [10],
                   ["banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana", "banana",
                    "banana"]))

    # 직접 입력
    # want = list(input().split())
    # number = list(map(int, input().split()))
    # discount = list(input().split())
    # print(solution(want, number, discount))


if __name__ == "__main__":
    main()
