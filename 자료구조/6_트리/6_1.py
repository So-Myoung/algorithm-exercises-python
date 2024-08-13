# 트리 - 트리 순회


# 전위 순회
def preorder(nodes, idx):
    if idx < len(nodes):
        res = str(nodes[idx]) + " "
        res += preorder(nodes, idx * 2 + 1)  # 재귀 호출
        res += preorder(nodes, idx * 2 + 2)
        return res
    else:
        return ""


# 중위 순회
def inorder(nodes, idx):
    if idx < len(nodes):
        res = inorder(nodes, idx * 2 + 1)
        res += str(nodes[idx]) + " "
        res += inorder(nodes, idx * 2 + 2)
        return res
    else:
        return ""


# 후위 순회
def postorder(nodes, idx):
    if idx < len(nodes):
        res = postorder(nodes, idx * 2 + 1)
        res += postorder(nodes, idx * 2 + 2)
        res += str(nodes[idx]) + " "
        return res
    else:
        return ""


def solution(nodes):
    return [
        preorder(nodes, 0)[:-1],
        inorder(nodes, 0)[:-1],
        postorder(nodes, 0)[:-1],
    ]


def main():
    # 테스트 케이스 1
    print(solution([1, 2, 3, 4, 5, 6, 7]))
    # 테스트 케이스 2
    print(solution([1, 4, 8, 3, 5, 6, 7]))
    # 위 두 케이스는 완전 이진 트리인 경우
    # 루트에서 시작해서 왼쪽 노드부터 오른쪽 노드까지 순서를 매기면 완전 이진 트리(Complete binary tree)같은 경우는 리스트에서 빈 숫자가 없음


if __name__ == "__main__":
    main()
