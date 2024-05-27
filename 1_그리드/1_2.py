
# 실전문제 1-2
# 그리드 - 숫자 카드 게임 : 난이도 1

result = 0
n, m = map(int, input().split())

for i in range(n):
    m_list = list(map(int, input().split()))

    min_num= min(m_list)
    result = max(result, min_num)

print(result)