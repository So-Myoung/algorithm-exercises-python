# 프로그래머스 알고리즘 고득점 kit
# 정렬 - 가장 큰 수
# Likewise, a comparison function such as cmp(a, b) will return a negative value for less-than, zero if the inputs are equal, or a positive value for greater-than.
import functools


def compare(a, b):
    t1 = str(a) + str(b)
    t2 = str(b) + str(a)
    pp = (int(t1) > int(t2)) - (int(t1) < int(t2))
    return (int(t1) > int(t2)) - (int(t1) < int(t2))


def solution(numbers):
    # 커스텀 한 기준에 따라 오름차순 정렬, ex) [3, 30] -> (커스텀 기준) [30, 3]
    # 내림차순으로 바꿔준 후 문자열을 이어 붙여주어야 큰 수가 된다.
    sorted_list = sorted(numbers, key=functools.cmp_to_key(lambda a, b: compare(a, b)), reverse=True)
    res = ''.join(str(x) for x in sorted_list)
    # 테스트 케이스 3번 - 0000 출력 방지
    return "0" if int(res) == 0 else res


def main():
    # # 테스트 케이스 1
    print(solution([6, 10, 2]))
    # # 테스트 케이스 2
    print(solution([3, 30, 34, 5, 9]))
    # # 테스트 케이스 3
    print(solution([0, 0, 0, 0]))  # 숫자이므로 0000이 아니라 0으로 출력되어야 한다.


if __name__ == "__main__":
    main()
