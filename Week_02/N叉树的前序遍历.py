        """
        # Definition for a Node.
        class Node:
            def __init__(self, val=None, children=None):
                self.val = val
                self.children = children
        """

        # N叉树简洁递归
        class Solution:
            def preorder(self, root: 'Node') -> List[int]:
                if not root: return []
                res = [root.val]
                for node in root.children:
                    res.extend(self.preorder(node))
                return res

        # N叉树通用递归模板
        class Solution:
            def preorder(self, root: 'Node') -> List[int]:
                res = []

                def helper(root):
                    if not root:
                        return
                    res.append(root.val)
                    for child in root.children:
                        helper(child)

                helper(root)
                return res

        # N叉树迭代方法
        class Solution:
            def preorder(self, root: 'Node') -> List[int]:
                if not root:
                    return []
                s = [root]
                # s.append(root)
                res = []
                while s:
                    node = s.pop()
                    res.append(node.val)
                    # for child in node.children[::-1]:
                    #     s.append(child)
                    s.extend(node.children[::-1])
                return res




