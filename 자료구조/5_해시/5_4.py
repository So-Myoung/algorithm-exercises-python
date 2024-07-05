# 해시 - 신고 결과 받기
# 2022 KAKAO BLIND RECRUITMENT

def solution(id_list, report, k):
    reported_user = {}
    count = {}
    res = []

    for r in report:
        user_id, reported_id = r.split()
        if reported_id not in reported_user:
            reported_user[reported_id] = set()
        reported_user[reported_id].add(user_id)

    for reported_id, user_id_lst in reported_user.items():
        if len(user_id_lst) >= k:
            for user_id in user_id_lst:
                if user_id not in count:
                    count[user_id] = 1
                else:
                    count[user_id] += 1

    for i in range(len(id_list)):
        if id_list[i] not in count:
            res.append(0)
        else:
            res.append(count[id_list[i]])

    return res


def main():
    # 테스트 케이스 1
    print(solution(["muzi", "frodo", "apeach", "neo"],
                   ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "muzi neo", "apeach muzi"], 2))
    # 테스트 케이스 2
    print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))


if __name__ == "__main__":
    main()
