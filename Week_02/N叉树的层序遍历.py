"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None:
            return []
        queue = [root]                                     #初始化一个root
        out = []
        while queue:
            child = []                                     #该轮循环的结果集
            node = []                                      #为下一轮while循环提供新数据集
            for item in queue:                             #因为是N叉树,所以需要遍历
                child.append(item.val)
                if item.children: node += item.children
            out.append(child)
            queue = node                                   #重要!  赋值给新 收集到的 子节点数据
        return out







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


