
# 스택 - 괄호 짝 맞추기

def solution(s):
    stack = []

    for c in s:
        if c == "(":
            stack.append(c)
        elif c == ")":
            if not stack:
                return False
            else:
                stack.pop()

    if stack:
        return False
    else:
        return True


def main():
    s = input()
    print(solution(s))


if __name__ == "__main__":
    main()