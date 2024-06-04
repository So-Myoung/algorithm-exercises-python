
# 프로그래머스 알고리즘 고득점 kit
# 그리드 - 큰 수 만들기 : Level 2

def solution(number, k):
    stack = []

    for n in number:
        while stack and k > 0 and n > stack[-1]:
            stack.pop()
            k -= 1
        stack.append(n)

    return ''.join(stack[:len(stack) - k])

def main():
    number = input()
    k = int(input())
    print(solution(number, k))

if __name__ == "__main__":
    main()