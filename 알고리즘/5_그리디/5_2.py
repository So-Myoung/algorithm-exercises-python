
# 그리디 - 숫자 카드 게임

result = 0
n, m = map(int, input().split())

for i in range(n):
    m_list = list(map(int, input().split()))

    min_num= min(m_list)
    result = max(result, min_num)

print(result)
