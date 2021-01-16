# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
'''
解题思路：通过先序遍历我们可以找到root，根据root我们可以再中序找到当前root对应的左右子树，再递归对当前root的左右子树进行构造(递归的时候别想多，把看到的一堆想成一个整体就好,想好递归终止条件，剩下的让程序去做吧，不然容易把自己陷入死循环弄得一头雾水)。
本题也是一样，知道inorder中，当前root的左侧的所有点就是其左子树，root的右侧的所有点就是当前root的右子树，就把这左右两堆数字想成当前root的左右2个节点就好，然后扔到函数里进行下一层的递归。
直接看代码比较清楚些。
inorder.index(preorder[0]) 这一步获取根的索引值，题目说树中的各个节点的值都不相同，也确保了这步得到的结果是唯一准确的。而且这个idx还能当长度用相当于 左+根 的长度，因为 左+根 和 根+左 是等长的。
————摘自题解
'''
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        if not preorder or not inorder:  # 递归终止条件
            return
        root = TreeNode(preorder[0])  # 先序为“根左右”，所以根据preorder可以确定root
        idx = inorder.index(preorder[0])  # 中序为“左根右”，根据root可以划分出左右子树
        # 下面递归对root的左右子树求解即可
        root.left = self.buildTree(preorder[1:1 + idx], inorder[:idx])
        root.right = self.buildTree(preorder[1 + idx:], inorder[idx + 1:])
        return root

