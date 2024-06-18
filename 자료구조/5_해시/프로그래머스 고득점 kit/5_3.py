
# 프로그래머스 알고리즘 고득점 kit
# 해시 - 전화번호 목록 : Level 2


def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1][:len(phone_book[i])]:
            return False
    return True

# def solution(phone_book):
#     phone_book.sort()
#     for p1, p2 in zip(phone_book, phone_book[1:]):
#         if p2.startswith(p1):
#             return False
#     return True


def main():
    # 테스트 케이스 1
    print(solution(["119", "97674223", "1195524421"]))
    # 테스트 케이스 2
    print(solution(["123", "456", "789"]))
    # 테스트 케이스 3
    print(solution(["12", "123", "1235", "567", "88"]))


if __name__ == "__main__":
    main()
