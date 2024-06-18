
# 정렬 - 문자열 내 마음대로 정렬하기
# 인덱스 1의 문자가 같은 문자열이 여럿 일 경우, 사전순으로 앞선 문자열이 앞쪽에 위치

def solution(strings, n):
    return sorted(strings, key=lambda x: (x[n], x))
# 비교할 요소가 복수 개일 경우, 튜플로 우선 순위를 정해줄 수 있음 : (x[n], x)


def main():
    # 테스트 케이스 1
    print(solution(["sun", "bed", "car"], 1))

    # 테스트 케이스 2
    print(solution(["abce", "abcd", "cdx"], 2))


if __name__ == "__main__":
    main()
