# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
  #递归
        res = []
        def helper(root):
            if not root:return
            res.append(root.val)
            helper(root.left)
            helper(root.right)
        helper(root)
        return res






   #迭代
        res = []
        p = root
        stack = []
        while p or stack:
            while p:
                res.append(p.val)
                stack.append(p)
                p = p.left
            p = stack.pop().right
        return res


