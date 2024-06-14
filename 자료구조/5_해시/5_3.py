
# 해시 - 오픈 채팅방
# 2019 KAKAO BLIND RECRUITMENT

def solution(record):
    res = []
    user = {}

    for cmd in record:
        c = cmd.split(' ')
        if c[0] != 'Leave':
            user[c[1]] = c[2]

    # 출력
    for cmd in record:
        c = cmd.split(' ')
        if c[0] == 'Enter':
            res.append(f'{user[c[1]]}님이 들어왔습니다.')
        elif c[0] == 'Leave':
            res.append(f'{user[c[1]]}님이 나갔습니다.')
        else:
            pass

    return res


def main():
    # 테스트 케이스
    record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
    print(solution(record))


if __name__ == "__main__":
    main()