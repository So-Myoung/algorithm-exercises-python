
# 실전문제 1-3
# 그리드 - 1이 될 때 까지 : 난이도 1

n, k = map(int, input().split())
result = 0

while n >= k:
    if n % k != 0:
        n -= 1
        result += 1

    else:
        n //= k
        result += 1

while n > 1:
    n -= 1
    result += 1

print(result)