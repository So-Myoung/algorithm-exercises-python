# 스택 - 괄호 회전하기

def solution(s):
    answer = 0
    n = len(s)

    for i in range(n):
        stack = []

        for j in range(n):
            c = s[(i + j) % n]

            if c == '[' or c == '(' or c == '{':
                stack.append(c)
            else:
                if not stack:
                    break

                if c == ']' and stack[-1] == '[':
                    stack.pop()
                elif c == ')' and stack[-1] == '(':
                    stack.pop()
                elif c == '}' and stack[-1] == '{':
                    stack.pop()
                else:
                    break
        else:
            if not stack:
                answer += 1

    return answer


def main():
    # 테스트 케이스 1
    print(solution("[](){}"))
    # 테스트 케이스 2
    print(solution("}]()[{"))
    # 테스트 케이스 3
    print(solution("[)(]"))
    # 테스트 케이스 4
    print(solution("}}}"))


if __name__ == "__main__":
    main()
