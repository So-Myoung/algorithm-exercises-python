
# 스택 - 10진수를 2진수로 변환하기
# stack, pop 사용
# 문자열 += 연산 시 수행할 때 마다 객체 새로 생성 -> 시간 복잡도 O((logN)^2)

def solution(d):
    stack = []
    result = ""

    while d > 0:
        r = d % 2
        stack.append(str(r))
        d //= 2

    while stack:
        result += stack.pop()

    return result

def main():
    d = int(input())
    print(solution(d))


if __name__ == "__main__":
    main()