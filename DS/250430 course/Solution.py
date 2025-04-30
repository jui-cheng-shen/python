class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        result = []
        def preorder(node):
            if not node:
                return
            result.append(node.val)
            preorder(node.left)
            preorder(node.right)
        preorder(root)
        return result

    def inorderTraversal(self, root):
        result = []
        def inorder(node):
            if not node:
                return
            inorder(node.left)
            result.append(node.val)
            inorder(node.right)
        inorder(root)
        return result

    def postorderTraversal(self, root):
        result = []
        def postorder(node):
            if not node:
                return
            postorder(node.left)
            postorder(node.right)
            result.append(node.val)
        postorder(root)
        return result

if __name__ == "__main__":
    # 構建二叉樹：
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    solution = Solution()

    print("preorder", solution.preorderTraversal(root))  # 輸出: [1, 2, 4, 5, 3]
    print("inorder", solution.inorderTraversal(root))    # 輸出: [4, 2, 5, 1, 3]
    print("postorder", solution.postorderTraversal(root))  # 輸出: [4, 5, 2, 3, 1]