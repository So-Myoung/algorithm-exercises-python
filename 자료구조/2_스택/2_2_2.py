
# 스택 - 10진수를 2진수로 변환하기
# list, join 사용
# 시간 복잡도 O(logN)
# '구분자'.join(리스트)

def solution(d):
    list = []

    while d > 0:
        r = d % 2
        list.append(str(r))
        d //= 2

    return ''.join(reversed(list))

def main():
    d = int(input())
    print(solution(d))


if __name__ == "__main__":
    main()