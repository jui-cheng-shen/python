class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.ltag = 0  # 0 表示左子樹，1 表示前驅
        self.rtag = 0  # 0 表示右子樹，1 表示後繼

class ThreadedBinaryTree:
    def __init__(self):
        self.root = None
        self.prev = None

    def create_tree(self):
        self.root = Node('A')

        self.root.left = Node('B')
        self.root.right = Node('C')

        self.root.left.left = Node('D')
        self.root.left.right = Node('E')

        self.root.right.left = Node('G')
        self.root.right.right = Node('F')

        self.root.left.left.left = Node('H')

        self.root.left.right.right = Node('I')

        self.root.right.left.left = Node('J')

    def create_threaded(self):
        self.prev = None
        self.inorder_thread(self.root)
        if self.prev:
            self.prev.rtag = 1
            self.prev.right = None

    def inorder_thread(self, node):
        if not node:
            return
        self.inorder_thread(node.left)

        if not node.left:
            node.ltag = 1
            node.left = self.prev

        if self.prev and not self.prev.right:
            self.prev.rtag = 1
            self.prev.right = node

        self.prev = node
        self.inorder_thread(node.right)

    def inorder(self):
        if not self.root:
            return
        current = self.root
        while current.ltag == 0:
            current = current.left

        while current:
            print(current.data, end=" ")
            if current.rtag == 1:
                current = current.right
            else:
                current = current.right
                while current and current.ltag == 0:
                    current = current.left

# 主程式
if __name__ == "__main__":
    tree = ThreadedBinaryTree()
    tree.create_tree()
    tree.create_threaded()
    print("中序遍歷結果（應為 H D B E I A J G C F）：")
    tree.inorder()
