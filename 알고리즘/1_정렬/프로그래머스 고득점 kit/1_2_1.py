
# 프로그래머스 알고리즘 고득점 kit
# 정렬 - 가장 큰 수
# 커스텀한 기준으로 sorting 할 수 있는 cmp_to_key 사용

def solution(numbers):
    number_list = list(map(str, numbers))
    number_list.sort(key=lambda x: x * 3, reverse=True)

    # 테스트 케이스 3번 - 0000 출력 방지
    # 1. int 형변환 + str 형변환
    return str(int(''.join(number_list)))

    # 2. int 형변환 + 3항 연산자
    # res = ''.join(number_list)
    # return "0" if int(res) == 0 else res


def main():
    # 테스트 케이스 1
    print(solution([6, 10, 2]))
    # 테스트 케이스 2
    print(solution([3, 30, 34, 5, 9]))
    # 테스트 케이스 3
    print(solution([0, 0, 0, 0]))  # 숫자이므로 0000이 아니라 0으로 출력되어야 한다.


if __name__ == "__main__":
    main()
