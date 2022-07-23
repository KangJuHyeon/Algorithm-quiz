# leetcode: Binary Tree Preorder Traversal

# Root -> Left -> Right (preorder 전위표기법)
# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorderTraversal(self, root: List[TreeNode]) -> List[int]:
        if not root: return []

        stack = [root]
        footage = []

        while stack:
            cur_node = stack.pop()
            if cur_node:
                footage.append(cur_node.val)
                stack.append(cur_node.right)
                stack.append(cur_node.left)

        return footage