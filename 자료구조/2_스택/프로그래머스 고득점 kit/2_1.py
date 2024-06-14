
# 프로그래머스 알고리즘 고득점 kit
# 스택 - 주식 가격 : Level 2

def solution(prices):
    n = len(prices)
    res = [0 for _ in range(n)]
    stack = [0]

    for i in range(1, n):
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()
            res[j] = i - j
        stack.append(i)

    while stack:
        j = stack.pop()
        res[j] = n - 1 - j

    return res

def main():
    prices = list(map(int, input().split()))
    print(solution(prices))

if __name__ == "__main__":
    main()