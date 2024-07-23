# 해시 - 문자열 해싱을 이용한 검색 함수 만들기

def polynomial_hash(str):
    p = 31
    m = 1_000_000_007
    hash_value = 0

    for char in str:
        hash_value = (hash_value * p + ord(char) % m)

    return hash_value


def solution(string_list, query_list):
    answer = []
    hash_list = [polynomial_hash(str) for str in string_list]

    for query in query_list:
        query_hash = polynomial_hash(query)
        if query_hash in hash_list:
            answer.append(True)

        else:
            answer.append(False)

    return answer


def main():
    # 테스트 케이스 1
    print(solution(['apple', 'banana', 'cherry'], ['banana', 'kiwi', 'melon', 'apple']))


if __name__ == "__main__":
    main()
