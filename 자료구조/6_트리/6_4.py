
# 트리 - 다단계 칫솔 판매

def solution(enroll, referral, seller, amount):
    parent = dict(zip(enroll, referral))

    total = {name: 0 for name in enroll}

    for i in range(len(seller)):
        money = amount[i] * 100
        cur_name = seller[i]

        while money > 0 and cur_name != '-':
            total[cur_name] += money - (money // 10)
            cur_name = parent[cur_name]
            money //= 10

    return [total[name] for name in enroll]


def main():
    # 테스트 케이스 1
    print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
                   ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
                   ["young", "john", "tod", "emily", "mary"],
                   [12, 4, 2, 5, 10]))
    # 테스트 케이스 2
    print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
                   ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
                   ["sam", "emily", "jaimie", "edward"],
                   [2, 3, 5, 4]))


if __name__ == "__main__":
    main()