'''
（例1）依下列給的後序及中序，畫出唯一的二元樹
後序：D E B G I H F C A

中序：D B E A G F I H C

'''

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder, postorder):
        # 創建中序序列中每個節點的索引映射
        inorder_map = {val: idx for idx, val in enumerate(inorder)}

        def build(post_start, post_end, in_start, in_end):
            # 基本情況：如果子樹範圍無效，返回 None
            if post_start > post_end or in_start > in_end:
                return None

            # 後序的最後一個節點是當前子樹的根
            root_val = postorder[post_end]
            root = TreeNode(root_val)

            # 在中序中找到根節點的位置
            root_idx = inorder_map[root_val]

            # 計算左子樹的節點數
            left_tree_size = root_idx - in_start

            # 遞迴構建左子樹
            root.left = build(post_start, 
                            post_start + left_tree_size - 1, 
                            in_start, 
                            root_idx - 1)

            # 遞迴構建右子樹
            root.right = build(post_start + left_tree_size, 
                                post_end - 1, 
                                root_idx + 1, 
                                in_end)

            return root
        # 調用遞迴函數，傳入初始範圍
        return build(0, len(postorder) - 1, 0, len(inorder) - 1)

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
    # 題目給定的後序和中序序列
    postorder = ['D', 'E', 'B', 'G', 'I', 'H', 'F', 'C', 'A']
    inorder = ['D', 'B', 'E', 'A', 'G', 'F', 'I', 'H', 'C']
    
    # 創建 Solution 實例
    solution = Solution()
    
    # 構建二元樹
    root = solution.buildTree(inorder, postorder)
    
    # 驗證構建的樹是否正確
    print("Inorder traversal of constructed tree:", solution.inorderTraversal(root))
    print("Postorder traversal of constructed tree:", solution.postorderTraversal(root))