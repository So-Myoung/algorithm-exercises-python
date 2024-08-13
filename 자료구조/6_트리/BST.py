# 트리 - 이진 탐색 트리(Binary Search Tree, BST) 구축/탐색

# 노드 클래스
class Node:
    def __init__(self, key):  # 생성자
        self.parent = key
        self.left = None
        self.right = None


# 이진 탐색 트리(BST) 클래스
class BST:
    def __init__(self):  # 생성자
        self.root = None

    # BST 구축
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            cur = self.root

            while True:
                if key < cur.parent:  # 기준 노드(부모 노드)보다 크기가 작으면 왼쪽(left) 자식 노드
                    if cur.left:
                        cur = cur.left
                    else:
                        cur.left = Node(key)
                        break
                else:
                    if cur.right:  # 기준 노드(부모 노드)보다 크기가 같거나 크면 오른쪽(right) 자식 노드
                        cur = cur.right
                    else:
                        cur.right = Node(key)
                        break

    # BST 탐색
    def search(self, key):
        cur = self.root

        # 노드가 존재하지 않거나 key = 현재 노드일 경우 loop 탈출
        # 탐색 값이 기준 노드 보다 작을 경우 왼쪽 자식 노드, 같거나 클 경우 오른쪽 자식 노드로 내려가 탐색
        while cur and cur.parent != key:
            if key < cur.parent:
                cur = cur.left
            else:
                cur = cur.right

        if cur:
            return cur.parent  # BST를 탐색하여 key 값과 일치하는 노드를 return
        else:
            return False  # 존재하지 않을 경우 False return


def solution(node_list, search_val):
    bst = BST()

    # 구축
    for key in node_list:
        bst.insert(key)

    # 탐색
    return bst.search(search_val)


def main():
    # 테스트 케이스 1
    print(solution([5, 3, 8, 4, 2, 1, 7, 10], 5))
    # 테스트 케이스 2
    print(solution([5, 3, 8, 4, 2, 1, 7, 10], 6))


if __name__ == "__main__":
    main()
