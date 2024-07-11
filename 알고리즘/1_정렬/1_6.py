# 정렬 - 튜플
# 2019 카카오 개발자 겨울 인턴십

def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s = sorted(s, key=len)

    for element in s:
        numbers = element.split(',')
        for number in numbers:
            if int(number) not in answer:
                answer.append(int(number))

    return answer


def main():
    # 테스트 케이스 1
    print(solution("{{2},{2,1},{2,1,3},{2,1,3,4}}"))
    # 테스트 케이스 2
    print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))
    # 테스트 케이스 3
    print(solution("{{20,111},{111}}"))
    # 테스트 케이스 4
    print(solution("{{123}}"))
    # 테스트 케이스 5
    print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))


if __name__ == "__main__":
    main()
