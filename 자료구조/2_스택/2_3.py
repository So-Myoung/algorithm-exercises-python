
# 스택 - 짝지어 제거하기

def solution(s):
    stack = []

    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
        else:
            stack.append(c)

    return int(not stack)

def main():
    s = input()
    print(solution(s))

if __name__ == "__main__":
    main()